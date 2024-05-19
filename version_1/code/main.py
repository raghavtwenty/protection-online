"""
Project Name: Protection Online
Filename: main.py
Title: Main streamlit UI
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
from _1_url_domain_split import extract_domain_url
from _2_webscrap import extract_web_text
from _3_web_details import weburl_info
from _4_security_check import url_input
from _5_llm import llm_privacy_prompt
import streamlit as st
import pandas as pd


# UI Configuration
st.set_page_config(
    page_title="Protection Online",
    layout="wide",
)
st.title("Protection Online")
st.write("Developed by: Raghava • GitHub: @raghavtwenty")
st.write("Date Created: January 10, 2024 • Last Updated: January 30, 2024")


# Streamlit app
def main():

    # User input
    url = st.text_input(
        "Website URL", placeholder="Enter the privacy policy link here..."
    )

    if st.button("Analyze"):
        # Text extraction
        extracted_text = extract_web_text(url)

        if extracted_text:
            col1, col2, col3 = st.tabs(
                ["Website Information", "Data Collection Report", "Security Report"]
            )

            # Website Information
            with col1:
                url, domain = extract_domain_url(url)
                st.text(f"Analyzing the Domain Name: {domain}")
                domain_info = weburl_info(url, domain)

                st.text(domain_info)

            # Data collection report
            with col2:
                llm_summary_output = llm_privacy_prompt(extracted_text)
                st.text(llm_summary_output)

            # Security report
            with col3:

                counts = url_input(url)
                data = []
                temp_text = ""

                for category, count in counts.items():
                    data.append({"CATEGORY": category.upper(), "SAFETY POINTS": count})

                df = pd.DataFrame(data)
                st.table(df)

        else:
            st.text("Couldn't extract URL, Check the URL or your internet connection.")


# Main
if __name__ == "__main__":
    main()
