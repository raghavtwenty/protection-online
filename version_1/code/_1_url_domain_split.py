"""
Project Name: Protection Online
Filename: _1_url_domain_split.py
Title: Preprocess the input url for security check
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""


# Url extraction
def extract_domain_url(url):
    split_content = url.split("/")
    url = split_content[0] + "//" + split_content[2]
    domain = split_content[2]
    return url, domain


# Main
if __name__ == "__main__":
    # Test case
    print(extract_domain_url("https://google.com/hi"))
