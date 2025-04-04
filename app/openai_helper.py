from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def get_resume_suggestions(resume_text, job_title="Machine Learning Engineer"):
    prompt = f"""
You are a professional resume coach. Below is the raw resume content and a target job title. Provide:
1. Specific improvements
2. Missing keywords or skills
3. Formatting tips (if any)

Resume Text:
{resume_text}

Target Job Title:
{job_title}

Suggestions:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
