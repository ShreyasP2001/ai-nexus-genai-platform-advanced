# AI Nexus – Advanced GenAI Business Intelligence Platform

**AI Nexus** is an agentic and generative AI platform that enables you to chat with business documents, forecast trends, extract insights from PDFs and CSVs, and even transcribe voice notes using OpenAI Whisper – all through a user-friendly Streamlit interface.

---

## 📁 Folder Structure

```
ai-nexus-genai-platform-advanced/
├── app/                      # Streamlit UI
│   └── app.py
├── data/                     # Upload sample CSVs and PDFs
├── export/                   # Auto-generated reports (PDF/CSV)
├── notebooks/                # Walkthrough demo notebook
│   └── demo.ipynb
├── results/                  # Visualizations, charts
├── src/                      # Core Python scripts
│   ├── rag_pipeline.py
│   ├── vector_db.py
│   ├── pdf_parser.py
│   ├── tts_whisper.py
│   ├── forecast.py
│   ├── user_auth.py
│   └── utils.py
├── vector_db/               # Vector index files
├── requirements.txt         # Python dependencies
├── .env.template            # API key configuration template
└── README.md                # This documentation
```

---

## 🚀 Setup Instructions (Step-by-Step)

### 🔧 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/ai-nexus-genai-platform-advanced.git
cd ai-nexus-genai-platform-advanced
```

### 🐍 Step 2: Set Up Python Virtual Environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

pip install -r requirements.txt
```

### 🔐 Step 3: Configure API Keys
Rename `.env.template` to `.env` and add your OpenAI key:
```
OPENAI_API_KEY=your-openai-api-key
```

---

## ▶️ Running the App

```bash
streamlit run app/app.py
```

Visit `http://localhost:8501` in your browser.

---

## 🧪 Features

### 📄 Chat with Documents
- Upload `.txt` files
- Ask natural language questions
- Uses RAG (retrieval-augmented generation) via LangChain + OpenAI

### 📈 Forecasting
- Upload time series CSV data (e.g., dates vs revenue)
- Predict future values using linear regression
- Visual plots + downloadable outputs

### 🧾 PDF Intelligence
- Upload a business PDF
- Extract and summarize content
- Ask questions about the PDF

### 🎙️ Voice Transcription
- Upload `.mp3`, `.wav`, `.m4a`
- Transcribe with Whisper model
- Copy/paste usable output

---

## 📘 Example Files for Testing

Add your test files inside the `data/` folder:
- `sample.csv` – for forecasting
- `sample.pdf` – for PDF parsing
- `sample.txt` – for RAG chat

---

## ✅ Requirements

- Python 3.8+
- OpenAI API key
- Internet access for model inference

---

## 📩 Contact & License

- Author: [Your Name]
- Contact: team@ainexus.ai
- License: MIT

© 2025 AI Nexus – All rights reserved.
