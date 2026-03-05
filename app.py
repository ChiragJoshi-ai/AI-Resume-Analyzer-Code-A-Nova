import streamlit as st
import tempfile

from resume_parser import extract_resume_text
from skill_matcher import calculate_similarity, extract_skills, missing_skills


st.title("🧠 AI Resume Analyzer")

st.write("Upload your resume and compare it with a job description.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

job_description = st.text_area("Paste Job Description")


if uploaded_file and job_description:

    with tempfile.NamedTemporaryFile(delete=False) as tmp:

        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    resume_text = extract_resume_text(temp_path)

    score = calculate_similarity(resume_text, job_description.lower())

    resume_skills = extract_skills(resume_text)

    missing = missing_skills(resume_skills, job_description.lower())


    st.subheader("📊 Resume Match Score")

    st.success(f"{score}% Match")


    st.subheader("✅ Skills Found")

    if resume_skills:
        for skill in resume_skills:
            st.write(f"- {skill}")
    else:
        st.write("No major skills detected")


    st.subheader("❌ Missing Skills")

    if missing:
        for skill in missing:
            st.write(f"- {skill}")
    else:
        st.write("Your resume already includes most required skills")


    if score < 40:
        st.warning("Low match. Resume may need improvement.")

    elif score < 70:
        st.info("Moderate match. Consider adding more relevant skills.")

    else:
        st.success("Great match! 🎉")