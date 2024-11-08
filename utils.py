import PyPDF2
import docx  # For Word files
import pandas as pd  # For CSV and Excel files

def read_pdf(file_path):
    """Reads a PDF file and returns the extracted text."""
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                # Extract text, handling cases where text extraction may fail
                extracted_text = page.extract_text() or ""
                text += extracted_text
    except Exception as e:
        print(f"Error reading PDF file '{file_path}': {e}")
        text = "" 
    return text.strip()

def read_docx(file_path):
    """Reads a Word (.docx) file and returns the extracted text."""
    text = ""
    try:
        doc = docx.Document(file_path)
        text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
    except Exception as e:
        print(f"Error reading Word file '{file_path}': {e}")
    return text.strip()

def read_csv(file_path):
    """Reads a CSV file and returns its content as a string."""
    try:
        df = pd.read_csv(file_path)
        return df.to_string(index=False)
    except Exception as e:
        print(f"Error reading CSV file '{file_path}': {e}")
        return ""

def read_excel(file_path):
    """Reads an Excel file and returns its content as a string."""
    try:
        df = pd.read_excel(file_path)
        return df.to_string(index=False)
    except Exception as e:
        print(f"Error reading Excel file '{file_path}': {e}")
        return ""

def process_text(input_text):
    """Preprocesses the text input by stripping whitespace."""
    return input_text.strip()

def read_text_file(file_path):
    """Reads a plain text (.txt) file and returns its content."""
    text = ""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except Exception as e:
        print(f"Error reading text file '{file_path}': {e}")
    return text.strip()

