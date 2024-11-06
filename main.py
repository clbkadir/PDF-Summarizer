import streamlit as st
from utils import extract_text
from utils import summarization
import os


def main():
    st.title('Text Summarization App')
    
    upl_file=st.file_uploader("Upload your document in PDF format", type="pdf")
    
    if upl_file is not None:
        text=extract_text(upl_file)    
        if text:
            with st.spinner("Summarizing..."):
                summary=summarization(text)
            st.subheader("Summary")
            st.write(summary)
            

if __name__ == "__main__":
    main()

    