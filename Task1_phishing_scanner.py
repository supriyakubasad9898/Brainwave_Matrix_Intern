import requests
import tldextract
from urllib.parse import urlparse

# A simple function to check if a URL is in a known phishing database
def check_known_phishing(url):
    # This is a placeholder for a real phishing database check
    # You can use APIs like PhishTank or Google Safe Browsing
    # For demonstration, we will just return False
    return False

# Function to analyze the URL
def analyze_url(url):
    # Extract domain
    extracted = tldextract.extract(url)
    domain = extracted.domain
    suffix = extracted.suffix

    # Check for common phishing indicators
    if len(domain) > 63 or len(suffix) > 6:
        return True  # Suspicious length

    # Check for known phishing URLs
    if check_known_phishing(url):
        return True  # Known phishing URL

    # Check for URL structure
    parsed_url = urlparse(url)
    if parsed_url.scheme not in ['http', 'https']:
        return True  # Not a valid scheme

    # Additional checks can be added here

    return False  # URL seems safe

# Main function to run the scanner
def main():
    print("=" * 50)
    print(" " * 10 + "Welcome to the Phishing Scanner")
    print(" " * 10 + "by Supriya Kubasad")
    print("=" * 50)
    
    url = input("Enter a URL to scan: ")
    print("\nAnalyzing the URL... Please wait...\n")
    
    if analyze_url(url):
        print("=" * 50)
        print("Warning: This URL may be a phishing link!")
        print("=" * 50)
    else:
        print("=" * 50)
        print("This URL appears to be safe.")
        print("=" * 50)
    
    print("Thank you for using the scanner!")
    print("Visit us again to scan another URL.")
    print("=" * 50)

if __name__ == "__main__":
    main()