"""
Project Name: Protection Online
Filename: _4_security_check.py
Title: Check input url using virus total api
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
import requests
import os
from dotenv import load_dotenv


# Env variables
load_dotenv()
api_key = os.getenv("VIRUS_TOTAL_API_KEY")


# Virus total checkup
def check_url_with_virustotal(url):
    global res_vt

    # Set up the VirusTotal API endpoint
    endpoint = "https://www.virustotal.com/vtapi/v2/url/report"

    # Set up the parameters for the API request
    params = {"apikey": api_key, "resource": url}

    try:
        # Make the request to VirusTotal
        response = requests.get(endpoint, params=params)
        result = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            # Check the scan results
            if result["response_code"] == 1:
                # URL is known by VirusTotal, print scan results
                res_vt = {}
                for scanner, result in result["scans"].items():
                    res_vt[scanner] = result["result"]
                    # print(f"{scanner}: {result['result']}")
            else:
                res_vt = "API limit exceeded."
        else:
            # Print the error message
            temp = result["verbose_msg"]
            res_vt = f"Error: {temp}"

    except Exception as e:
        res_vt = f"An error occurred: {e}"
    return res_vt


# Input and output format
def url_input(url):

    res_vt = check_url_with_virustotal(url)

    # Count occurrences of each category - unrated/unrated/suspicious site
    category_counts = {}
    for category in res_vt.values():
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1

    return category_counts


# Main
if __name__ == "__main__":
    # Test case
    print(url_input("https://www.google.com"))
