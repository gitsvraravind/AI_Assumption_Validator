# AI_Assumption_Validator
AI Assumption Validator is a Streamlit web application that analyzes business documents to identify explicit and hidden assumptions, assess decision risk, and (optionally) recommend actions to reduce that risk.  

## 🚀 Why This Project Exists

Business documents often look polished but contain:
- Unstated assumptions
- High-risk dependencies
- Missing evidence
- Gaps in decision rationale

These issues usually surface **after** problems occur.

This app helps surface them **before approval**.

## 🧩 Key Features

### 🔍 Assumption Analysis
- Identifies **explicit assumptions**
- Infers **implicit / hidden assumptions**
- Flags **high-risk assumptions** with risk levels
- Highlights **missing validations or evidence**
- Surfaces **decision-critical questions**

### 🎛️ Two Analysis Modes
- **Analysis Only**  
  Focuses purely on identifying assumptions and risks.

- **Analysis + Recommendations**  
  Adds targeted, actionable suggestions on:
  - What should be changed
  - Where it should be addressed
  - What evidence or validation is needed

### 📂 Document Support
- Microsoft Word (`.docx`)
- PDF (`.pdf`)

## 📸 App Preview (Optional)
*(Add a screenshot here once deployed)*
<img width="1851" height="435" alt="image" src="https://github.com/user-attachments/assets/314948df-2449-40c0-9e59-a12c05bb1e2b" />
## 🧪 Sample Test File

A sample document (`sample_assumptions.docx`) is included in the repository to quickly test the app.

Example content:
- Strategy assumptions
- Capacity assumptions
- Timeline and regulatory assumptions

## 📄Install Dependencies
- pip install -r requirements.txt
- Set OpenAI API Key
.streamlit/secrets.toml
 OPENAI_API_KEY = "your_openai_api_key"
- Run the app
python -m streamlit run app.py

## 🛠️ Structure
ai-assumption-validator/
│
├── app.py
├── requirements.txt
├── README.md
├── sample_assumptions.docx
├── .gitignore
└── .streamlit/
    └── secrets.toml   (not committed)
