import PyPDF2
import os
from dotenv import load_dotenv


load_dotenv()

def read_pdf(file_path):
    """Reads a PDF file and returns the extracted text."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                # Safely extract text to handle cases where extraction might fail
                extracted_text = page.extract_text() or ""
                text += extracted_text
    except Exception as e:
        print(f"Error reading PDF file '{file_path}': {e}")
        text = "" 
    return text.strip()  

def process_text(input_text):
    """Preprocess the text input if needed. Currently, it just strips whitespace."""
    return input_text.strip()

def read_text_file(file_path):
    """Reads a text file and returns its content."""
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading text file '{file_path}': {e}")
    return text.strip()  # Trim the result to remove any leading/trailing whitespace
