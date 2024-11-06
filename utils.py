import pdfplumber
from transformers import pipeline
import io

# Extract text from uploaded files (only 1000 tokens extracted due to limit error)

def extract_text(pdf_file):
    text=""
    pdf_data = io.BytesIO(pdf_file.read()) 
    with pdfplumber.open(pdf_data) as pdf:  
        for page in pdf.pages:
            text += page.extract_text() + "\n"    
    return text[:1000]


# Define summarization model and summarize  text by LLM

def summarization(text, min=30, max=150):
    summarizer=pipeline("summarization",model="facebook/bart-large-cnn")
    summary= summarizer(text,min_length=min,max_length=max)
    return summary[0]['summary_text']

