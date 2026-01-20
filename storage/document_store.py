import sqlite3
import json
from config.settings import DB_PATH
from core.json_utils import make_json_safe

def save_document(document):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    """)

    safe_document = make_json_safe(document)

    c.execute(
        "INSERT INTO documents (content) VALUES (?)",
        (json.dumps(safe_document),)
    )

    conn.commit()
    conn.close()
