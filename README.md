# 📄 Resume Analyzer (AI-Powered)

Resume Analyzer is a smart web app that uses Natural Language Processing (NLP) to extract and analyze key details from resumes. It's perfect for HRs, recruiters, and job portals looking to automate resume screening.

---

## 🚀 Features

- 🔍 Extracts candidate details (Name, Email, Skills, etc.)
- 🧠 NLP-powered parsing using spaCy
- 🖥️ Clean and interactive Streamlit web UI
- 📤 Upload and analyze `.pdf` resumes in seconds

---

## 🛠️ Tech Stack

- Python 🐍
- Streamlit 🌐
- spaCy 🧠
- PyPDF2 📄

---

---

## 📌 How It Works

1. **Upload Your Resume**  
   The user uploads a `.pdf` or `.docx` resume file using the file uploader in the Streamlit interface.

2. **Automatic Parsing**  
   The app uses `spaCy` (NLP) to extract:
   - Name
   - Email address
   - Phone number
   - Total pages
   - Skills (based on keywords)

3. **Results Displayed Instantly**  
   Once parsed, the details are shown immediately on the same page in a clean, readable format.

4. **Skill Visualization**  
   The app highlights extracted skills for easy screening by HR or clients.

5. **No Data Stored**  
   All processing is done locally — resume data is not stored or uploaded anywhere.

---



## 📁 Project Structure

```bash
resume-analyzer-app/
├── app.py                # Streamlit frontend
├── resume_parser.py      # Resume parsing logic (spaCy & PyPDF2)
├── sample_resume.pdf     # Example resume
├── requirements.txt      # Python dependencies
└── README.md             # You're here!
