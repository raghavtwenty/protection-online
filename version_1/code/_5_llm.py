"""
Project Name: Protection Online
Filename: _5_llm.py
Title: Get the response from the llm
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
import replicate
import os
from dotenv import load_dotenv


# Env variables
load_dotenv()
api_key = os.getenv("REPLICATE_API_TOKEN")


# Get the summary
def llm_summary(extracted_text, prompt):
    extracted_text += prompt
    summary = ""

    # LLM Model - Mixtral
    for event in replicate.stream(
        "mistralai/mixtral-8x7b-instruct-v0.1",
        input={"prompt": extracted_text},
    ):
        summary += str(event)

    return summary


# Prompts
def llm_privacy_prompt(extracted_text):
    prompt = "tell me the data collected from the user by the above given website domain.  In 5 points with 5 min of reading content short and sweet. The points should be understandable to the common users. Each point should be of atmost 15 words not more than that. Output format: Data Collected: "

    llm_output = llm_summary(extracted_text, prompt)
    return llm_output


# Main
if __name__ == "__main__":
    # Test case
    print(llm_privacy_prompt("google privacy policy"))
