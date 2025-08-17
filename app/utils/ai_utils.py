# import os
# from openai import OpenAI

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# client = OpenAI(api_key=OPENAI_API_KEY)

# def extract_missing_keywords(resume_text: str, job_description: str) -> str:
#     prompt = f"""
#     You are an expert resume reviewer.
#     Compare the following RESUME with the JOB DESCRIPTION.
#     Extract important keywords/skills from the JOB DESCRIPTION that are MISSING in the RESUME.
#     Return them as a comma-separated list only.

#     RESUME: {resume_text}
#     JOB DESCRIPTION: {job_description}
#     """

#     response = client.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=[{"role": "user", "content": prompt}],
#         max_tokens=200
#     )

#     keywords = response.choices[0].message.content.strip()
#     return [kw.strip() for kw in keywords.split(",") if kw.strip()]

# ------------------- Below code for Huggingface use ------------------

from sentence_transformers import SentenceTransformer, util
import re

# Load once (fast, cached)
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def clean_text(text: str) -> list[str]:
    """Extract lowercase words without punctuation"""
    return re.findall(r"\b\w+\b", text.lower())

def extract_missing_keywords(resume_text: str, job_description: str) -> list[str]:
    # Extract words
    resume_words = set(clean_text(resume_text))
    jd_words = clean_text(job_description)

    # Candidates: words in JD but not in resume
    missing_candidates = [w for w in jd_words if w not in resume_words and len(w) > 3]

    if not missing_candidates:
        return []

    # Embed resume + candidate words
    resume_embedding = model.encode(resume_text, convert_to_tensor=True)
    candidate_embeddings = model.encode(missing_candidates, convert_to_tensor=True)

    # Compute cosine similarity
    similarities = util.cos_sim(candidate_embeddings, resume_embedding).cpu().numpy().flatten()

    # Pair words with similarity
    scored = list(zip(missing_candidates, similarities))

    # Sort by lowest similarity (least covered in resume → more "missing")
    scored_sorted = sorted(scored, key=lambda x: x[1])

    # Return top 20 missing keywords
    return [word for word, _ in scored_sorted[:20]]
