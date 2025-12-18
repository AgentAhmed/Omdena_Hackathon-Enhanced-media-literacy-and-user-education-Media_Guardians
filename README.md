# 🛡️ Omdena_Hackathon-Enhanced-media-literacy-and-user-education-Media_Guardians


### AI-Driven Text & Document Analysis for Media Literacy

🔗 **Live App:**  
👉 https://omdena-ai-agent-ahmed.streamlit.app/

---

## 📌 Project Overview

**AI-Driven Text and Document Analysis** is an AI-powered web application developed during the **Omdena Hackathon** to enhance **media literacy and critical thinking**.

In an era of misinformation and information overload, this tool helps users:
- Understand the **sentiment** behind content  
- **Fact-check** claims and statements  
- Gain **educational insights** for deeper understanding  

The app supports **text, PDFs, documents, spreadsheets, and URLs**, making it a practical tool for students, researchers, journalists, and everyday users.

---

## 🚀 Key Features

### 🧠 Sentiment Analysis
- Identifies emotional tone and bias in content  
- Helps users recognize manipulative or misleading language  

### 🔍 Fact-Checking
- Verifies claims and statements using AI reasoning  
- Highlights potential misinformation or unsupported claims  

### 🎓 Educational Insights
- Provides context, explanations, and learning-oriented insights  
- Encourages critical thinking rather than blind consumption  

### 📄 Multi-Format Support
- ✅ Plain text  
- ✅ PDF documents  
- ✅ Word files (DOCX)  
- ✅ CSV & Excel files  
- ✅ Web URLs  

### 📥 Downloadable Reports
- Generate and download **PDF analysis reports**  
- Useful for documentation, sharing, and academic work  

### 🖥️ Clean & User-Friendly Interface
- Built with Streamlit  
- Simple workflow: upload → analyze → review → download  

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---------|--------|
| **Python** | Core backend logic |
| **Streamlit** | Web application framework |
| **Groq API** | Large Language Model inference |
| **LLaMA 3.3 (70B)** | NLP analysis |
| **PyPDF2** | PDF text extraction |
| **python-docx** | DOCX file processing |
| **pandas** | CSV & Excel handling |
| **BeautifulSoup** | Web content extraction |
| **FPDF / FPDF2** | PDF report generation |
| **dotenv** | Environment variable management |

---

## 🧩 How the App Works (Workflow)

1. **Input Content**
   - Paste text OR
   - Upload a file OR
   - Enter a URL

2. **AI Processing**
   - Content is chunked for large inputs
   - Each chunk is analyzed independently

3. **AI Outputs**
   - Sentiment Analysis
   - Fact-Checking Results
   - Educational Insights

4. **Export**
   - Download full analysis as a **PDF report**

---

## 🔐 API Key Management

This app uses the **Groq API**.

### Local Setup
Create a `.env` file:
```env
GROQ_API_KEY=your_api_key_here
