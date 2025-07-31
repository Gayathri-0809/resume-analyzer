# app.py

import streamlit as st
from resume_parser import extract_text_from_docx, extract_name, extract_email, extract_phone, extract_skills

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("📄 Resume Analyzer")
st.markdown("Upload a `.docx` resume to analyze key info like name, email, phone number, and skills.")

uploaded_file = st.file_uploader("Choose a .docx file", type="docx")

if uploaded_file is not None:
    with st.spinner("Analyzing Resume..."):
        text = extract_text_from_docx(uploaded_file)

        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)

        st.subheader("Extracted Information:")
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Phone:** {phone}")
        st.write(f"**Skills:** {', '.join(skills)}")

        st.success("Done! ✅")
