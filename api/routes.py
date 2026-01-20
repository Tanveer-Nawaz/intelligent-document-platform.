from fastapi import APIRouter, UploadFile, File

from core.ingestion import ingest_document
from core.segmentation import segment_document
from core.summarization import generate_summaries
from core.ner import extract_entities
from core.insights import extract_insights
from core.json_utils import make_json_safe
from storage.document_store import save_document

router = APIRouter()

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    text, metadata = ingest_document(file)
    sections, chunks = segment_document(text)

    summaries = generate_summaries(sections)
    entities = extract_entities(text)
    insights = extract_insights(text)

    document = {
        "metadata": metadata,
        "sections": sections,
        "summaries": summaries,
        "entities": entities,
        "insights": insights
    }

    safe_document = make_json_safe(document)
    save_document(safe_document)

    return safe_document
