# 🧠 AI Resume Analyzer

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![NLP](https://img.shields.io/badge/NLP-Scikit--Learn-green)
![UI](https://img.shields.io/badge/UI-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A simple **AI-powered Resume Analyzer** that compares a candidate's resume with a job description and calculates a **match score** using Natural Language Processing techniques.

The system extracts text from a resume PDF, analyzes skills, and highlights **missing skills required for the job role**.

---

## 🚀 Features

- 📄 Upload resume in **PDF format**
- 🧠 **NLP-based similarity scoring**
- 📊 Resume **match score calculation**
- ✅ **Skill extraction**
- ❌ **Missing skill suggestions**
- 🌐 Simple web interface using **Streamlit**

---

## 🛠 Tech Stack

| Technology | Purpose |
|-------------|------------|
| **Python** | Core programming language |
| **Streamlit** | Web interface |
| **Scikit-learn** | Cosine similarity for NLP |
| **PDFMiner** | Resume text extraction |
| **NLTK** | Text preprocessing |

---

## 📂 Project Structure

resume-analyzer  
│  
├── app.py              # Main Streamlit application  
├── resume_parser.py    # Extracts text from resume PDFs  
├── skill_matcher.py    # Handles similarity scoring & skill detection  
├── skills.py           # Skill database used for matching  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation

Clone the repository

git clone https://github.com/ChiragJoshi-ai/AI-Resume-Analyzer-Code-A-Nova/

Install dependencies using **uv**

uv pip install streamlit pdfminer.six scikit-learn pandas nltk

---

## ▶️ Run the Application

Start the Streamlit server

uv run streamlit run app.py

The app will open in your browser:

http://localhost:8501

---

## 🧪 How It Works

1. Upload a resume (PDF)  
2. Paste the job description  
3. The system extracts resume text  
4. Cosine similarity calculates the **match score**  
5. Skills are extracted and missing skills are highlighted  

---

## 📊 Example Output

Match Score: 78%

Skills Found:
python  
docker  
sql  
git  

Missing Skills:
kubernetes  
tensorflow  

---

## 🔮 Future Improvements

- ATS-style resume scoring  
- Better skill extraction using spaCy  
- Multiple resume ranking system  
- Resume improvement suggestions  
- Enhanced UI dashboard  

---

## 👨‍💻 Author

**Chirag Joshi**  
B.Tech Computer Science Engineering 

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**.
