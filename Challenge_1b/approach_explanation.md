# Approach Explanation

## Objective

The system aims to extract and rank the most relevant sections and subsections from a collection of PDFs based on a persona and their job-to-be-done.

## Methodology

1. **PDF Parsing**: Using PyMuPDF to extract raw text from each page with page numbers.

2. **Persona Intent Construction**: We combine persona and job as a query string:
   _"As a [persona], my task is to [job]"_

3. **Embedding & Similarity**:

   - Use `sentence-transformers` (MiniLM, < 100MB) for fast, CPU-compatible sentence embeddings.
   - Compute cosine similarity between the persona intent and section texts.

4. **Ranking**:

   - Rank top 5 sections globally across documents.
   - Within each section, further analyze and extract the most relevant paragraph as refined text.

5. **Output**:
   - JSON includes metadata, extracted section details, and granular sub-section snippets.

## Constraints Handling

- **Offline Mode**: No internet access; all models are pre-installed.
- **CPU only**: All processing is compatible with CPU execution.
- **< 1GB**: Model size is ~80MB, well under the limit.
- **60s runtime**: Efficient batch processing ensures time compliance.

## Generalization

The system uses semantic similarity and is fully domain-agnostic. It handles documents from travel, HR onboarding, recipes, research, and finance.
