import os
import time
from json_utils import load_input_json, save_output_json
from pdf_utils import extract_pdf_text
from ranker import rank_sections
from datetime import datetime


COLLECTIONS = ["Collection 1", "Collection 2", "Collection 3"]

def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")
    input_data = load_input_json(input_path)

    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    intent = f"As a {persona}, my task is to {job}"

    all_sections = []
    all_paragraphs = []
    for doc in input_data["documents"]:
        pdf_path = os.path.join(collection_path, "PDFs", doc["filename"])
        pages = extract_pdf_text(pdf_path)

        for page in pages:
            section_title = page["text"].split('\n')[0].strip()[:100]
            all_sections.append({
                "document": doc["filename"],
                "page_number": page["page_number"],
                "section_title": section_title,
                "text": page["text"]
            })

    extracted_sections, subsection_analysis = rank_sections(all_sections, intent)

    output_json = {
        "metadata": {
            "input_documents": [doc["filename"] for doc in input_data["documents"]],
            "persona": persona,
            "job_to_be_done": job,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    save_output_json(output_path, output_json)
    print(f"✅ Processed {collection_path}")

if __name__ == "__main__":
    start = time.time()
    for collection in COLLECTIONS:
        process_collection(os.path.join(".", collection))
    end = time.time()
    print(f"\n⏱ Total processing time: {end - start:.2f} seconds")
