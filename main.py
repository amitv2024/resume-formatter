import json
import os

from pypdf import PdfReader
from response_structure import Resume
from google import genai
from google.genai import types

def extract_resume_text(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text

def structure_resume(resume_text):
    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    prompt = f"""
Extract the information from the following resume.

Rules:
- Do not invent information.
- If information is not present, use null.
- Extract all relevant skills.
- Summarize every work experience entry.
- Extract every education entry.
- Preserve the meaning of the candidate's experience.
- From all of the above entries derive strenths and weaknesses.

Resume:
----------------
{resume_text}
----------------
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Resume,
        ),
    )
    return Resume.model_validate_json(response.text)


resume_text = extract_resume_text("resume.pdf")
resume = structure_resume(resume_text)
print(resume)