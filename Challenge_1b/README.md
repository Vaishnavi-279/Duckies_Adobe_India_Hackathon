# Persona-Driven Document Intelligence

## 📌 Overview

This project is part of Round 1B of Adobe's "Connecting the Dots" Hackathon. It builds a CPU-only, offline system to extract and rank the most relevant sections from a set of PDFs, based on a given persona and their job-to-be-done.

## 📂 Directory Structure

```
persona-extractor/
├── Dockerfile
├── requirements.txt
├── main.py
├── utils.py (optional)
├── model/ (optional)
├── Challenge_1b/
│   ├── Collection 1/
│   │   ├── PDFs/
│   │   ├── challenge1b_input.json
│   │   └── challenge1b_output.json
│   ├── Collection 2/
│   └── Collection 3/
├── approach_explanation.md
└── README.md
```

## ⚙️ Setup Instructions

### 🐳 Docker Build

Make sure you're in the root directory (where Dockerfile is located):

```bash
docker build -t persona-intel:round1b .
```

> If your system blocks DNS or fails to resolve DockerHub, check your Docker DNS settings or restart Docker.

### ▶️ Docker Run

Run your solution for each collection like this (Windows example):

```bash
docker run --rm -v "%cd%/Challenge_1b/Collection 1:/app/Collection 1" -e COLLECTION_PATH="/app/Collection 1" persona-intel:round1b
```

For Linux/macOS:

```bash
docker run --rm -v "$(pwd)/Challenge_1b/Collection 1:/app/Collection 1" -e COLLECTION_PATH="/app/Collection 1" persona-intel:round1b
```

### 🛠 Example Input

Your `challenge1b_input.json` should look like:

```json
{
  "documents": [{ "filename": "guide1.pdf" }, { "filename": "guide2.pdf" }],
  "persona": {
    "role": "Travel Blogger",
    "expertise": "Cultural exploration"
  },
  "job_to_be_done": {
    "task": "Create a 7-day itinerary for the South of France"
  }
}
```

The `challenge1b_output.json` will be generated after successful execution.

## 📦 Dependencies

Defined in `requirements.txt`. Installed during Docker build:

```txt
sentence-transformers==2.2.2
PyMuPDF==1.22.0
scikit-learn==1.3.0
tqdm==4.66.1
numpy==1.26.4
huggingface-hub==0.10.1
pdfminer.six==20221105
```

## Constraints Met

- Offline
- CPU-only
- <1GB model
- Executes within 60 seconds

---

## 📞 Contact

Built by \[Your Name], Duckies Team 🐥

> "Connecting ideas. Reading minds."
