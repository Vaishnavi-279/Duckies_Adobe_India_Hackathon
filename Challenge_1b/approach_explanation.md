# Approach Explanation for Challenge 1B: Persona-Driven Document Intelligence

## Overview

This solution aims to extract and rank the most relevant sections from a collection of PDFs based on a given persona and their job-to-be-done. The entire pipeline is designed to be offline, efficient, and run within the specified constraints of model size, time, and CPU-only execution.

---

## Methodology

### 1. **Input Parsing**

Each collection folder contains:

- A set of PDFs (under `PDFs/` directory).
- A `challenge1b_input.json` file specifying:

  - List of document filenames
  - Persona's role and expertise
  - A specific task (job-to-be-done)

The input JSON is loaded using a utility (`json_utils.py`) which extracts the relevant fields.

### 2. **PDF Text Extraction**

PDFs are parsed using the **PyMuPDF (fitz)** library, which efficiently extracts page-wise text content. Each page is considered a potential section for analysis.

For each page:

- The first line of text is used as the section title.
- The entire page's content is retained for ranking.

### 3. **Intent Construction**

The user's intent is formulated as a single string combining persona and job:

```
As a [persona], my task is to [job-to-be-done]
```

This natural language description acts as a semantic query against the content.

### 4. **Ranking Relevant Sections**

All extracted sections are ranked based on similarity to the constructed intent using:

- **SentenceTransformers (`all-MiniLM-L6-v2`)**: a lightweight transformer-based model (\~100MB), ideal for fast and meaningful semantic embedding.
- Cosine similarity is computed between intent embedding and each section's text embedding.
- Top-ranked sections are returned as the most relevant.

### 5. **Sub-section Analysis**

For each top-ranked section:

- Key phrases or refined summaries are extracted.
- These are added to a `subsection_analysis` output.

### 6. **Output Formatting**

The final `challenge1b_output.json` is structured as:

- Metadata (input documents, persona, job, timestamp)
- Ranked relevant sections with title, doc name, page number, rank
- Sub-section analysis for deeper insight

---

## Constraints Handling

- Offline Mode: No internet access used
- CPU-only execution: All models run on CPU
- Model size < 200MB: Uses `all-MiniLM-L6-v2`
- Runtime < 60 seconds: Tested on 3–5 PDFs successfully

---

## Dependencies

- `PyMuPDF` for PDF parsing
- `sentence-transformers` for semantic ranking
- `scikit-learn` and `numpy` for similarity and ranking
- `tqdm` for progress tracking

---

## Summary

This solution provides a generalizable pipeline to transform unstructured PDF data into ranked insights tailored to specific personas. It is lightweight, modular, and built for adaptability across different document domains and tasks.
