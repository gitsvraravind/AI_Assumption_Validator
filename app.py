import streamlit as st
import openai
from docx import Document
from PyPDF2 import PdfReader

# ----------------------------
# Page Config (MUST BE FIRST)
# ----------------------------
st.set_page_config(
    page_title="AI Assumption Validator",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🧠 AI Assumption Validator")
st.caption(
    "Identify hidden assumptions and decision risks in business documents."
)

# ----------------------------
# OpenAI Configuration
# ----------------------------
openai.api_key = st.secrets["OPENAI_API_KEY"]

# ----------------------------
# Analysis Mode Toggle
# ----------------------------
analysis_mode = st.radio(
    "Select Analysis Mode",
    ["Analysis Only", "Analysis + Recommendations"],
    horizontal=True
)

# ----------------------------
# Prompt Builders
# ----------------------------
def get_analysis_only_prompt(document_text, doc_type):
    return f"""
You are a senior management consultant specializing in decision quality and risk assessment.

Your objective is NOT to summarize the document.
Your objective is to evaluate the quality of assumptions underlying the decision-making.

Analyze the following {doc_type} and produce the following sections:

1. Explicit Assumptions
2. Implicit / Hidden Assumptions
3. High-Risk Assumptions
   - Classify each as Low / Medium / High risk
   - Explain why in one sentence
4. Missing Validations or Evidence
5. Decision-Critical Questions

Guidelines:
- Do NOT summarize.
- Do NOT provide recommendations or rewrites.
- Be concise, structured, and practical.
- Use bullet points.

Document:
{document_text}
"""

def get_analysis_with_recommendations_prompt(document_text, doc_type):
    return f"""
You are a senior management consultant specializing in decision quality and risk assessment.

Your objective is NOT to summarize the document.
Your objective is to evaluate assumptions and recommend actions that reduce decision risk.

Analyze the following {doc_type} and produce the following sections:

1. Explicit Assumptions
2. Implicit / Hidden Assumptions
3. High-Risk Assumptions
   - Classify each as Low / Medium / High risk
   - Explain why in one sentence

4. Recommended Risk-Reduction Actions
   - For each High-Risk assumption:
     - What should be changed or added
     - Where in the document it should be addressed
     - What evidence or validation is needed

5. Decision-Critical Questions

Guidelines:
- Do NOT summarize.
- Do NOT rewrite the full document.
- Be concise, structured, and practical.
- Use bullet points.

Document:
{document_text}
"""

# ----------------------------
# Utility Functions
# ----------------------------
def extract_text_from_docx(file):
    doc = Document(file)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def analyze_assumptions(document_text, doc_type, analysis_mode):
    if analysis_mode == "Analysis Only":
        prompt = get_analysis_only_prompt(document_text, doc_type)
    else:
        prompt = get_analysis_with_recommendations_prompt(document_text, doc_type)

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    return response.choices[0].message.content

# ----------------------------
# UI Inputs
# ----------------------------
doc_type = st.selectbox(
    "Select Document Type",
    ["Strategy Document", "Business Proposal", "Project Plan", "Other"]
)

uploaded_file = st.file_uploader(
    "Upload Document (Word or PDF)",
    type=["docx", "pdf"]
)

analyze_btn = st.button("🔍 Analyze Document")

# ----------------------------
# Main Logic
# ----------------------------
if analyze_btn:
    if not uploaded_file:
        st.error("Please upload a document.")
    else:
        if uploaded_file.type == "application/pdf":
            document_text = extract_text_from_pdf(uploaded_file)
        else:
            document_text = extract_text_from_docx(uploaded_file)

        if len(document_text.strip()) < 300:
            st.warning("Document seems very short. Results may be limited.")

        with st.spinner("Analyzing assumptions and risks..."):
            analysis = analyze_assumptions(
                document_text,
                doc_type,
                analysis_mode
            )

        st.subheader("📌 Assumption Analysis Report")
        st.markdown(analysis)