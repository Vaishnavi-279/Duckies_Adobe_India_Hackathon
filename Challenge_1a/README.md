Challenge 1a: PDF Processing Solution
Overview
This solution implements Challenge 1a of Adobe India Hackathon 2025. The goal is to extract structured outline data from PDF documents and output JSON files for each PDF. The solution is fully containerized with Docker and meets the official constraints on execution time, resource usage, and architecture.

Official Challenge Guidelines
Submission Requirements
GitHub Project: Complete project with working code

Dockerfile: Present in root directory and functional

README.md: Documentation explaining approach, models, libraries, and usage

Build Command
bash

docker build --platform linux/amd64 -t <reponame.someidentifier>

Run Command

bash
docker run --rm -v $(pwd)/input:/app/input:ro -v $(pwd)/output/repoidentifier/:/app/output --network none <reponame.someidentifier>
Critical Constraints
Execution time ≤ 10 seconds for 50-page PDFs

Model size ≤ 200MB (no ML models used here)

No internet access during runtime

CPU-only (amd64), tested on 8 CPUs, 16GB RAM

Compatible with AMD64 architecture (no ARM-specific code)

Input directory is read-only

Key Solution Features
Automatically processes all PDFs from /app/input directory

Generates JSON output files named after each PDF in /app/output

Uses open source libraries only

Tested on simple and complex PDF layouts

Sample Implementation Details
PDF Text Extraction: Using PyMuPDF (fitz), extracts text spans and font sizes from each page

Heading Detection: Sorts unique font sizes, maps top 3 sizes to headings H1, H2, H3

Outline Generation: Creates JSON with headings, levels, and page numbers

Title Detection: Picks first H1 heading as title or falls back to PDF metadata

Sample Dockerfile
dockerfile

FROM python:3.10-slim

WORKDIR /app

requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
Sample requirements.txt
nginx

pymupdf
Expected Output Format
Each processed PDF generates a corresponding .json file matching the schema below:

json

{
"title": "Document Title",
"outline": [
{ "level": "H1", "text": "Heading 1", "page": 1 },
{ "level": "H2", "text": "Subheading", "page": 2 },
{ "level": "H3", "text": "Sub-subheading", "page": 3 }
]
}
Testing Instructions
Build Docker Image
bash

docker build --platform linux/amd64 -t mysolutionname:tag .
Run Docker Container
bash

docker run --rm \
 -v $(pwd)/input:/app/input:ro \
 -v $(pwd)/output:/app/output \
 --network none \
 mysolutionname:tag
Processes all PDFs in /app/input (read-only)

Saves JSON outlines in /app/output

Project Structure
css

Round1A/
├── main.py
├── Dockerfile
├── requirements.txt
├── README.md
