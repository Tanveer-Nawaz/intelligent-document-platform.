import re

def extract_insights(text):
    sentences = [s.strip() for s in text.split(".")]

    risks = [s for s in sentences if any(w in s.lower() for w in ["risk", "limitation", "challenge"])]
    decisions = [s for s in sentences if any(w in s.lower() for w in ["will", "aims to", "proposed"])]
    recommendations = [s for s in sentences if "recommend" in s.lower()]

    return {
        "deadlines": [],
        "risks": risks[:5],
        "decisions": decisions[:5],
        "recommendations": recommendations[:5]
    }

