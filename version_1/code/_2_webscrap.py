"""
Project Name: Protection Online
Filename: _2_webscrap.py
Title: For the given url extract all the text from website
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
from bs4 import BeautifulSoup
import requests


# Text extraction
def extract_web_text(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        for script in soup(["script", "style"]):  # CSS not required
            script.extract()

        text = soup.get_text(separator="\n", strip=True)

    except requests.exceptions.RequestException as e:
        text = st.error(f"Error fetching URL: {e}")

    return text


# Main
if __name__ == "__main__":
    # Test case
    print(extract_web_text("https://google.com/"))
