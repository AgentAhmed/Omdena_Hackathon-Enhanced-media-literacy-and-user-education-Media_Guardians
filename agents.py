import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader
import docx  # For Word files
import pandas as pd  # For CSV and Excel files
import requests
from bs4 import BeautifulSoup

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

class SentimentAgent:
    def analyze_text(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": text}],
                model="llama3-8b-8192"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Sentiment Analysis Error: {str(e)}"}

class FactCheckAgent:
    def check_facts(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Fact-check: {text}"}],
                model="llama3-8b-8192"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Fact-Checking Error: {str(e)}"}

class EducationAgent:
    def analyze_for_education(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Educational insights: {text}"}],
                model="llama3-8b-8192"
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Education Analysis Error: {str(e)}"}

def process_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = "".join(page.extract_text() for page in reader.pages if page.extract_text())
        return text.strip()
    except Exception as e:
        return {"error": f"PDF Processing Error: {str(e)}"}

def process_docx(docx_file):
    try:
        doc = docx.Document(docx_file)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
        return text.strip()
    except Exception as e:
        return {"error": f"Word Processing Error: {str(e)}"}

def process_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        return df.to_string(index=False)
    except Exception as e:
        return {"error": f"CSV Processing Error: {str(e)}"}

def process_excel(excel_file):
    try:
        df = pd.read_excel(excel_file)
        return df.to_string(index=False)
    except Exception as e:
        return {"error": f"Excel Processing Error: {str(e)}"}

def process_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        text = ' '.join([p.get_text() for p in soup.find_all('p')])
        return text.strip()
    except Exception as e:
        return {"error": f"URL Processing Error: {str(e)}"}


