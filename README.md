# 📧 Email Triage AI Environment

## 🚀 Overview
This project is an AI-powered email classification environment built using FastAPI. It simulates real-world email triaging where an agent classifies emails as spam, urgent, or normal.

## ⚙️ Features
- 📩 Email simulation environment
- 🤖 Baseline AI agent
- 🧪 Grading system for evaluation
- 🎯 Difficulty levels (easy, medium, hard)
- 🌐 REST API using FastAPI

## 🧠 How it Works
1. `/reset` → Get an email
2. `/step` → Classify email + respond
3. `/grader` → Evaluate response
4. `/baseline` → Auto AI response

## 🛠️ Tech Stack
- Python
- FastAPI
- Uvicorn

## ▶️ Run Locally
```bash
pip install -r requirements.txt
python3 -m uvicorn app:app --reload


https://harshithayadav28-email-env.hf.space/docs

https://email-env.onrender.com/docs#/
