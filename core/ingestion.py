import pdfplumber
import docx
import os
from config.settings import UPLOAD_DIR

def ingest_document(file):
    filepath = os.path.join(UPLOAD_DIR, file.filename)
    with open(filepath, "wb") as f:
        f.write(file.file.read())

    text = ""

    if file.filename.endswith(".pdf"):
        with pdfplumber.open(filepath) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"

    elif file.filename.endswith(".docx"):
        doc = docx.Document(filepath)
        for para in doc.paragraphs:
            text += para.text + "\n"

    metadata = {
        "filename": file.filename,
        "length": len(text)
    }

    return text, metadata
