# 🧠 AI Cover Letter & Cold Email Generator

An intelligent web app that instantly generates **tailored cover letters** and **cold emails** for any job posting — all based on your uploaded resume and a job URL. Powered by LLaMA 3 via Groq and built with LangChain + Streamlit.

---

## 🚀 Features

- 📄 Upload your **PDF resume**
- 🔗 Paste any **job posting link**
- ✨ Instantly generate:
  - 🎯 A **customized cover letter**
  - ✉️ A **cold email**
- ✅ Choose what you want: Cover Letter, Cold Email, or both
- ⚡ Uses **LLaMA 3 (70B)** via **Groq API**
- 🎨 Clean, modern UI themed with yellow highlights
- 📋 Built-in **copy buttons** for easy use

---

## 🛠️ Tech Stack

| Layer        | Technology                                 |
|--------------|--------------------------------------------|
| Frontend     | Streamlit, HTML/CSS                        |
| Backend      | Python, LangChain, Flask (optional)        |
| LLM Provider | Groq + LLaMA 3 (70B)                       |
| Parsing      | PyMuPDF (PDF to text)                      |
| Scraping     | LangChain WebBaseLoader                    |
| Secrets Mgmt | dotenv                                     |
