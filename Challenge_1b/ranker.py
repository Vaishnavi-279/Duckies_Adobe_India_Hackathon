from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')

def rank_sections(sections, query, top_k=5):
    section_texts = [s["section_title"] + " " + s["text"][:500] for s in sections]
    section_embeddings = model.encode(section_texts, convert_to_tensor=True)
    query_embedding = model.encode([query], convert_to_tensor=True)

    similarities = cosine_similarity(query_embedding.cpu(), section_embeddings.cpu())[0]
    ranked = sorted(zip(similarities, sections), key=lambda x: x[0], reverse=True)

    extracted = []
    refined = []

    for rank, (score, section) in enumerate(ranked[:top_k], start=1):
        extracted.append({
            "document": section["document"],
            "section_title": section["section_title"],
            "importance_rank": rank,
            "page_number": section["page_number"]
        })

        # Subsection selection from section paragraphs
        for para in section["text"].split("\n\n"):
            if len(para.strip()) > 50:
                sim = cosine_similarity(
                    model.encode([query]),
                    model.encode([para])
                )[0][0]
                if sim > 0.4:
                    refined.append({
                        "document": section["document"],
                        "refined_text": para.strip()[:500],
                        "page_number": section["page_number"]
                    })
                    break  # one refined text per section

    return extracted, refined
