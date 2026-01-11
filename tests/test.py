# from fpdf import FPDF

# # Create instance of FPDF class
# pdf = FPDF()

# # Add a page
# pdf.add_page()

# # Set font
# pdf.set_font("Arial", size=12)

# # Add a cell
# pdf.cell(200, 10, txt="Hello World", ln=True, align="C")

# # Output PDF to file
# pdf.output("test.pdf")

import os
from dotenv import load_dotenv

load_dotenv()  # Ensure this is called before accessing environment variables

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    print("GROQ_API_KEY not found in environment variables.")
else:
    print(f"GROQ_API_KEY loaded successfully: {api_key}")

