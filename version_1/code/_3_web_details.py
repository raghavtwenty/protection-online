"""
Project Name: Protection Online
Filename: _3_web_details.py
Title: For the given url perform extract web details SSL, whois, http
Author: Raghava | GitHub: @raghavtwenty
Date Created: January 10, 2024 | Last Updated: May 19, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import whois
import tldextract
import ssl
import socket
import certifi


# URL information
def get_url_info(url):
    info = {}

    # Extract domain and subdomain information
    domain_info = tldextract.extract(url)
    info["domain"] = domain_info.domain
    info["subdomain"] = domain_info.subdomain

    try:
        # Send a GET request to the URL
        response = requests.get(url, allow_redirects=True)

        # Basic information
        info["status_code"] = response.status_code
        info["headers"] = dict(response.headers)
        info["content_type"] = response.headers.get("Content-Type")

        # Extract and parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        info["title"] = soup.title.string.strip() if soup.title else None
        info["meta_tags"] = [
            meta.get("name", "") for meta in soup.find_all("meta", {"name": True})
        ]

        # Whois information
        whois_info = whois.whois(url)
        info["whois"] = whois_info

    except requests.RequestException as e:
        info["error"] = f"Error: {e}"

    return info


# Perform SSL Validation
def check_ssl_validity(url):
    try:
        context = ssl.create_default_context(cafile=certifi.where())
        with context.wrap_socket(
            socket.socket(), server_hostname=urlparse(url).hostname
        ) as s:
            s.connect((urlparse(url).hostname, 443))
        return True

    except Exception as e:
        print(f"SSL Error: {e}")
        return False


# SSL Validation and full details
def validate_ssl_cert(hostname, port=443):
    try:
        # Create an SSL context
        context = ssl.create_default_context()
        text = ""

        # Establish a connection to the server
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get the SSL certificate from the server
                cert = ssock.getpeercert()

                # Check the validity of the certificate
                ssl.match_hostname(cert, hostname)

                text += "\nSSL Certificate Details:\n"
                text += f"Subject: {cert['subject']}\n"
                text += f"Issuer: {cert['issuer']}\n"
                text += f"Expiration Date: {cert['notAfter']}\n"
                text += "SSL Certificate Validation Successful.\n"

    except ssl.SSLCertVerificationError as e:
        text = "SSL Certificate Validation Failed: " + str(e)

    except socket.error as e:
        text = "Connection error: " + str(e)

    return text


# Input preprocess and setup output format
def weburl_info(url, domain_name):
    ssl_details = validate_ssl_cert(domain_name)
    ssl_valid = check_ssl_validity(url)
    ssl_valid_text = f"SSL Validity: {ssl_valid}\n"

    url_info = get_url_info(url)
    formatted_url_info = ""

    for key, value in url_info.items():
        if isinstance(value, dict):
            formatted_url_info += f"{key}:\n"
            for sub_key, sub_value in value.items():
                formatted_url_info += f"  {sub_key}: {sub_value}\n"
        else:
            formatted_url_info += f"{key}: {value}\n"

    output = ssl_details + "\n" + ssl_valid_text + "\n" + formatted_url_info
    return output


# Main
if __name__ == "__main__":
    # Test case
    print(weburl_info("https://google.com", "www.google.com"))
