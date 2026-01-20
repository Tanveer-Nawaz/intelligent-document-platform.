from transformers import pipeline
from config.settings import SUMMARIZATION_MODEL

summarizer = pipeline("summarization", model=SUMMARIZATION_MODEL)

def summarize_text(text, max_len=250, min_len=120):
    if len(text.strip()) < 200:
        return text

    summary = summarizer(
        text[:3500],
        max_length=max_len,
        min_length=min_len,
        do_sample=False
    )[0]["summary_text"]

    # Ensure clean sentence ending
    if "." in summary:
        summary = summary.rsplit(".", 1)[0] + "."

    return summary

def generate_summaries(sections: dict):
    """
    sections = {
        "Introduction": "...",
        "Problem Statement": "...",
        ...
    }
    """

    # 🔹 Rebuild full document text
    full_text = "\n".join(sections.values())

    executive_summary = summarize_text(full_text, max_len=180, min_len=90)
    detailed_summary = summarize_text(full_text, max_len=350, min_len=180)

    section_summaries = {}
    for name, text in sections.items():
        section_summaries[name] = summarize_text(text, max_len=150, min_len=60)

    return {
        "executive_summary": executive_summary,
        "detailed_summary": detailed_summary,
        "section_summaries": section_summaries
    }
