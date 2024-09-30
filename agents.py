import os
from dotenv import load_dotenv
from groq import Groq
from PyPDF2 import PdfReader  # Updated PdfReader

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))  # Ensure the API key is correctly loaded

class SentimentAgent:
    def analyze_text(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": text}],
                model="llama3-8b-8192",  # Use Groq model
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Sentiment Analysis Error: {str(e)}"}

class FactCheckAgent:
    def check_facts(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Fact-check: {text}"}],
                model="llama3-8b-8192",  # Use Groq model
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Fact-Checking Error: {str(e)}"}

class EducationAgent:
    def analyze_for_education(self, text):
        try:
            chat_completion = client.chat.completions.create(
                messages=[{"role": "user", "content": f"Educational insights: {text}"}],
                model="llama3-8b-8192",  # Use Groq model
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            return {"error": f"Education Analysis Error: {str(e)}"}

# PDF Processing
def process_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() if page.extract_text() else ""  # Handle pages without text
        return text.strip()  # Return trimmed text
    except Exception as e:
        return {"error": f"PDF Processing Error: {str(e)}"}
