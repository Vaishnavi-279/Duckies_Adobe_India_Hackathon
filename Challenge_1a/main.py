# main.py
import fitz  # PyMuPDF
import os
import json

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)

    blocks = []
    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                text = ""
                font_sizes = []
                for span in line["spans"]:
                    text += span["text"]
                    font_sizes.append(span["size"])
                if text.strip():
                    avg_font = sum(font_sizes) / len(font_sizes)
                    blocks.append({
                        "text": text.strip(),
                        "font_size": avg_font,
                        "page": page_num
                    })

    # Step 1: Get unique font sizes
    sizes = sorted(set([b["font_size"] for b in blocks]), reverse=True)

    # Step 2: Map top 3 font sizes to H1, H2, H3
    heading_map = {}
    for i, size in enumerate(sizes[:3]):
        heading_map[size] = f"H{i+1}"

    # Step 3: Assign heading level
    outline = []
    for b in blocks:
        level = heading_map.get(b["font_size"])
        if level:
            outline.append({
                "level": level,
                "text": b["text"],
                "page": b["page"]
            })

    # Step 4: Guess title (first H1 or fallback)
    title = ""
    for item in outline:
        if item["level"] == "H1":
            title = item["text"]
            break
    if not title:
        title = doc.metadata.get("title") or "Unknown Title"

    return {
        "title": title,
        "outline": outline
    }

def main():
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(INPUT_DIR, filename)
            print(f"Processing {input_path}...")
            result = extract_outline(input_path)
            output_filename = filename.replace(".pdf", ".json")
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            print(f"Saved: {output_path}")

if __name__ == "__main__":
    main()
