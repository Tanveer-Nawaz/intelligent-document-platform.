import re

SECTION_HEADERS = [
    "Introduction",
    "Problem Statement",
    "Methodology",
    "Outcomes",
    "Conclusion"
]

def segment_document(text):
    sections = {}
    current_section = "Preamble"
    buffer = []

    for line in text.splitlines():
        clean = line.strip()

        if clean in SECTION_HEADERS:
            if buffer:
                sections[current_section] = "\n".join(buffer)
                buffer = []
            current_section = clean
        else:
            buffer.append(clean)

    if buffer:
        sections[current_section] = "\n".join(buffer)

    return sections, list(sections.values())
