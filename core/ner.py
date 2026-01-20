from transformers import pipeline

try:
    ner_pipeline = pipeline(
        "ner",
        model="dslim/bert-base-NER",
        aggregation_strategy="simple"
    )
    NER_AVAILABLE = True
except Exception:
    ner_pipeline = None
    NER_AVAILABLE = False


def extract_entities(text):
    doc = nlp(text)
    entities = []

    for ent in doc.ents:
        if len(ent.text) < 4:
            continue
        if ent.label_ == "MISC" and len(ent.text) < 10:
            continue

        entities.append({
            "text": ent.text,
            "label": ent.label_
        })

    return entities
