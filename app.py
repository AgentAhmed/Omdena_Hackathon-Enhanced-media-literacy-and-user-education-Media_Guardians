import streamlit as st
from agents import SentimentAgent, FactCheckAgent, EducationAgent, process_pdf
from groq import Groq
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize agents
sentiment_agent = SentimentAgent()
fact_check_agent = FactCheckAgent()
education_agent = EducationAgent()

# Streamlit app configuration for a wide layout and attractive title
st.set_page_config(page_title="AI-Driven Text and PDF Analysis for Media Literacy", layout="wide")
st.title("🌟 AI-Driven Text and PDF Analysis for Media Literacy 🌟")
st.write(
    """
    **Analyze text and PDF files for sentiment, fact-checking, and educational insights using advanced AI models.**
    """
)

# Input text for analysis
st.header("📄 Enter Text for Analysis")
text_input = st.text_area("Type or paste your text below:", height=200)

# PDF Upload section for analysis
st.header("📂 Upload a PDF File for Analysis")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

# Button to trigger the analysis process
if st.button("Analyze"):
    # If text is entered, analyze it
    if text_input:
        st.subheader("🧠 Sentiment Analysis Report")
        sentiment_result = sentiment_agent.analyze_text(text_input)  # Correct method call
        st.write(sentiment_result if not isinstance(sentiment_result, dict) else sentiment_result.get('error'))

        st.subheader("🔍 Fact-Checking Report")
        fact_check_result = fact_check_agent.check_facts(text_input)
        st.write(fact_check_result if not isinstance(fact_check_result, dict) else fact_check_result.get('error'))

        st.subheader("🎓 Educational Insights")
        education_result = education_agent.analyze_for_education(text_input)
        st.write(education_result if not isinstance(education_result, dict) else education_result.get('error'))


    # Analyze uploaded PDF if provided
    if uploaded_file:
        st.subheader("📑 PDF Analysis")
        pdf_text = process_pdf(uploaded_file)
        if isinstance(pdf_text, dict) and "error" in pdf_text:
            st.error(f"Failed to process PDF: {pdf_text['error']}")
        else:
            st.write("Extracted Text from PDF:")
            st.write(pdf_text)


st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        width: 100%;
        padding: 12px;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    .stTextInput textarea {
        border-radius: 10px;
        font-size: 16px;
        border: 1px solid #ccc; /* Adding a border */
    }
    .stFileUploader div {
        border-radius: 10px;
        border: 1px dashed #ccc; /* Dashed border for file uploader */
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)
