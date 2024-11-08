import warnings
warnings.filterwarnings("ignore")

import os
import streamlit as st
from io import BytesIO
from fpdf import FPDF  # To generate PDFs
from PyPDF2 import PdfFileWriter, PdfFileReader
from docx import Document  # To generate Word files
from agents import SentimentAgent, FactCheckAgent, EducationAgent, process_pdf, process_docx, process_csv, process_excel, process_url
import textwrap
import openpyxl



# Initialize agents
sentiment_agent = SentimentAgent()
fact_check_agent = FactCheckAgent()
education_agent = EducationAgent()

# Adjust page settings and title
st.set_page_config(page_title="AI-Driven Text Analysis for Media Literacy", layout="wide")

# # Use custom markdown to remove padding or adjust spacing
# st.markdown("<style> .stTitle { padding-top: 0px; } </style>", unsafe_allow_html=True)

st.markdown("""
    <h1 style='text-align: center; font-size: 28px; color: #00BFFF;'>🌟 AI-Driven Text and Document Analysis for Media Literacy 🤖</h1>
""", unsafe_allow_html=True)

# # Title section
# st.title("🌟 AI-Driven Text and Document Analysis for Media Literacy 🌟")

# st.set_page_config(page_title="AI-Driven Text Analysis for Media Literacy", layout="wide")
# st.title("🌟 AI-Driven Text and Document Analysis for Media Literacy 🌟")

st.sidebar.header("Input Options")
url_option = st.sidebar.checkbox("Analyze URL")
file_option = st.sidebar.checkbox("Upload File")
text_option = st.sidebar.checkbox("Enter Text", value=True)
voice_option = st.sidebar.checkbox("Use Voice Command")  # Placeholder for voice command
st.sidebar.header("Analysis Options")
default_option = st.sidebar.checkbox("Default (All)", value=True)
analyze_option = st.sidebar.checkbox("Analysis")
fact_check_option = st.sidebar.checkbox("Fact-Checking")
education_option = st.sidebar.checkbox("Educational Insights")
# If voice_option is selected, show a message saying the feature is coming soon
if voice_option:
    st.sidebar.info("🔊 Voice Command feature is coming soon! Stay tuned.")

# Function to chunk the content into smaller parts (for large text)
def chunk_text(text, chunk_size=1000):
    return textwrap.wrap(text, chunk_size)

# Function to analyze each chunk of text
def analyze_chunks(content_to_analyze):
    chunks = chunk_text(content_to_analyze)
    analysis_results = {
        "Analysis": [],
        "Fact-Checking": [],
        "Educational Insights": []
    }
    
    for chunk in chunks:
        sentiment_result = sentiment_agent.analyze_text(chunk)
        analysis_results["Analysis"].append(sentiment_result if not isinstance(sentiment_result, dict) else sentiment_result.get('error'))

        fact_check_result = fact_check_agent.check_facts(chunk)
        analysis_results["Fact-Checking"].append(fact_check_result if not isinstance(fact_check_result, dict) else fact_check_result.get('error'))

        education_result = education_agent.analyze_for_education(chunk)
        analysis_results["Educational Insights"].append(education_result if not isinstance(education_result, dict) else education_result.get('error'))
    
    return analysis_results

# Input sections based on sidebar options
content_to_analyze = None
analysis_results = {}

# if text_option:
#     st.header("📄 Enter Text for Analysis")
#     text_input = st.text_area("Type or paste your text below:", height=100)
#     if text_input:
#         content_to_analyze = text_input

# Enter Text Section with custom font size
if text_option:
    st.markdown("""
        <h2 style='font-size: 20px; color: #00BFFF;'>📄 Enter Text for Analysis</h2>
    """, unsafe_allow_html=True)
    text_input = st.text_area("Type or paste your text below:", height=100)
    if text_input:
        content_to_analyze = text_input

# URL input section with custom font size
if url_option:
    st.markdown("""
        <h2 style='font-size: 20px; color: #00BFFF;'>🌐 Enter URL for Content Analysis</h2>
    """, unsafe_allow_html=True)
# if url_option:
#     st.header("🌐 Enter URL for Content Analysis")
    url_input = st.text_input("Paste a URL to analyze its content:")
    if url_input:
        content_to_analyze = process_url(url_input)


# File upload section with custom font size
if file_option:
    st.markdown("""
        <h2 style='font-size: 20px; color: #00BFFF;'>📂 Upload a File for Analysis</h2>
    """, unsafe_allow_html=True)
# File upload section
# if file_option:
#     st.header("📂 Upload a File for Analysis")
    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "csv", "xlsx"])
    if uploaded_file:
        # Process the file based on its type
        if uploaded_file.type == "application/pdf":
            content_to_analyze = process_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            content_to_analyze = process_docx(uploaded_file)
        elif uploaded_file.type == "text/csv":
            content_to_analyze = process_csv(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            content_to_analyze = process_excel(uploaded_file)
        else:
            st.error("Unsupported file type. Please upload a PDF, DOCX, CSV, or XLSX file.")
            
        # Show confirmation message once the file is uploaded
        st.success("File uploaded successfully!")    

# Analysis section
if st.button("Run Analysis") and content_to_analyze:
    # If the content is a string, process the text
    if isinstance(content_to_analyze, str):
        # Apply chunking for large text (if applicable)
        analysis_results = analyze_chunks(content_to_analyze)

        # Display results
        if default_option or analyze_option:
            st.subheader("🧠 Analysis Report")
            st.write("\n".join(analysis_results["Analysis"]))

        if default_option or fact_check_option:
            st.subheader("🔍 Fact-Checking Report")
            st.write("\n".join(analysis_results["Fact-Checking"]))

        if default_option or education_option:
            st.subheader("🎓 Educational Insights")
            st.write("\n".join(analysis_results["Educational Insights"]))
    else:
        # If content extraction fails
        st.error(content_to_analyze.get("error", "Error occurred during content extraction"))


# Function to generate PDF
def generate_pdf(analysis_results):
    pdf = FPDF()

    # Set up Unicode font (ensure DejaVuSans.ttf is in the fonts folder)
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # # Add the font (replace 'fonts/DejaVuSans.ttf' with the correct path if needed)
    # font_path = os.path.join("fonts", "fonts/DejaVuSans.ttf")
    # pdf.add_font('DejaVu', '', font_path, uni=True)
    # pdf.set_font("DejaVu", size=12)
   # Dynamically calculate the font path relative to the script location
    font_path = os.path.join(os.path.dirname(__file__), "DejaVuSans.ttf")

    # Check if the font file exists (useful for debugging)
    if not os.path.exists(font_path):
        print(f"Font file not found at: {font_path}")
    else:
        print(f"Font file found at: {font_path}")

    # Add the font to the PDF (ensure the font file is in the correct path)
    pdf.add_font('DejaVu', '', font_path, uni=True)

    # Set the font to DejaVu and set the font size
    pdf.set_font("DejaVu", size=12)
    

    pdf.cell(200, 10, "AI-Driven Text Analysis Report", ln=True, align="C")
    pdf.ln(10)

    # Add content to the PDF
    for section, content in analysis_results.items():
        pdf.cell(0, 10, f"{section}:", ln=True)
        content_str = '\n'.join(content) if isinstance(content, list) else content
        pdf.multi_cell(0, 10, content_str)
        pdf.ln(5)

    # Create a BytesIO object to hold the generated PDF
    pdf_output = BytesIO()
    pdf.output(pdf_output, 'S')
    pdf_output.seek(0)

    return pdf_output

# Function to handle the download button click without page reset
def download_clicked():
    st.session_state["download_clicked"] = True

# Initialize session state for the download click if not already set
if "download_clicked" not in st.session_state:
    st.session_state["download_clicked"] = False

# Ensure analysis_results is defined elsewhere in your app
if 'analysis_results' in locals() and analysis_results:
    # Generate the PDF buffer in memory
    pdf_buffer = generate_pdf(analysis_results)
    
    # Provide the option to download the PDF in the sidebar with a unique key
    st.sidebar.download_button(
        label="Download as PDF",
        data=pdf_buffer,
        file_name="analysis_report.pdf",
        mime="application/pdf",
        key="unique_pdf_download",
        on_click=download_clicked
    )
    
    # Display message after download to confirm action
    if st.session_state["download_clicked"]:
        st.success("Click the download button to download the PDF report")
