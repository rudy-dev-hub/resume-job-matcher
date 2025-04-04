import streamlit as st
from app.resume_parser import parse_resume
from app.job_matcher import match_jobs
import tempfile
import os
from app.openai_helper import get_resume_suggestions

st.title("AI Resume Matcher")

st.markdown("""
Upload your resume in PDF format and see how well it matches job descriptions.
""")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:
    # Save uploaded file temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.success("Resume uploaded successfully!")
    parsed = parse_resume(tmp_path)

    st.subheader("Extracted Skills")
    st.write(parsed["skills"])

    st.subheader("Job Matches")
    matches = match_jobs(parsed, "data/job_descriptions.json")

    for job, score in matches:
        st.markdown(f"**{job['title']}** - Match Score: `{score}`")
        st.markdown(f"> {job['description']}")
        st.markdown("---")

    # Cleanup temp file
    os.remove(tmp_path)

st.subheader("💬 AI-Powered Suggestions")
job_title = st.text_input("🎯 Target Job Title", value="Machine Learning Engineer")
if st.button("Suggest Resume Improvements"):
    with st.spinner("Analyzing resume with GPT..."):
        
        tips = get_resume_suggestions(parsed["raw"], job_title=job_title)
        st.success("Here's how you can improve your resume:")
        st.markdown(tips)
