import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.job_scraper import scrape_job_description
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="🧠 AI Resume & Email Generator", layout="wide")

# Custom dark theme with yellow highlight
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #f1f1f1;
    }
    .stApp {
        background-color: #1e1e1e;
    }
    .st-bf {
        color: #f1f1f1;
    }
    .stButton>button {
        background-color: #facc15;
        color: black;
        font-weight: 600;
        border-radius: 8px;
    }
    .stTextArea textarea {
        background-color: #222;
        color: #facc15;
    }
    .stTextInput>div>div>input {
        background-color: #222;
        color: white;
    }
    .stMultiSelect>div>div>div>input {
        background-color: #222;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧠 AI Resume + Email Generator")

st.markdown("Upload your **resume** and paste the **job link** to get a tailored cold email and/or CV. 🎯")

# Input section
resume_file = st.file_uploader("📎 Upload Resume (PDF)", type=["pdf"])
job_url = st.text_input("🔗 Paste Job Posting URL")
output_option = st.multiselect("🧾 What do you want to generate?", ["Cold Email", "Tailored CV"])

# Generate button
if st.button("🚀 Generate") and resume_file and job_url and output_option:
    with st.spinner("Working on it..."):
        try:
            resume_text = extract_text_from_pdf(resume_file)
            job_description = scrape_job_description(job_url)

            llm = ChatGroq(
                model="llama3-70b-8192",
                temperature=0,
                groq_api_key=os.getenv("GROQ_API_KEY")
            )

            prompt = PromptTemplate.from_template("""
Given the following resume and job description, generate the following:

Resume:
{resume}

Job Description:
{job}

Outputs:
{output_type}
""")
            formatted_prompt = prompt.format(
                resume=resume_text,
                job=job_description,
                output_type=", ".join(output_option)
            )

            result = llm.invoke(formatted_prompt)

            st.success("✅ Generation complete!")

            st.subheader("📬 Generated Output")
            st.code(result.content, language="markdown")  # Adds copy button

        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.info("👈 Upload resume, paste job link, and select what to generate.")
