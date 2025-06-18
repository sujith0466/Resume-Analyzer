# Resume-Analyzer
# 🧠 AI Resume Analyzer

A Flask-based web application that uses **NLP** to analyze resumes (PDF or DOCX) and evaluate how well they match with job-specific keywords. Built without a database — lightweight, fast, and fully deployable!

![Demo Screenshot](https://user-images.githubusercontent.com/your-username/demo-image.png)

## 🚀 Features

- 📄 Upload resume (.pdf or .docx)
- 🧠 Extracts skills and experience using NLP
- 📊 Scores match with target job keywords
- 📋 Gives personalized suggestions for improvement
- 🔒 No database needed — works completely in memory

## 🛠️ Built With

- **Flask** – Python web framework
- **nltk** & **spaCy** – Natural Language Processing
- **pdfminer.six** & **docx2txt** – Resume parsing
- **gunicorn** – Production server for deployment

## 📁 Project Structure
ResumeAnalyzer/
├── app.py
├── resume_parser.py
├── target_keywords.json
├── uploads/
├── templates/
│ └── index.html
├── requirements.txt
