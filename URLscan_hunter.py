import requests
import time

# User-agent string to mimic a Google Chrome browser on Windows
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.212'

# URLScan.io API details
API_KEY = 'your_urlscan_api_key'
HEADERS = {
    'API-Key': API_KEY,
    'Content-Type': 'application/json'
}
SUBMIT_URL = 'https://urlscan.io/api/v1/scan/'
RESULT_URL = 'https://urlscan.io/api/v1/result/'

def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def log_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + "\n")

def submit_to_urlscan(url):
    response = requests.post(SUBMIT_URL, headers=HEADERS, json={'url': url})
    if response.status_code == 200:
        return response.json()['uuid']
    else:
        print(f"Error submitting {url} to URLScan: {response.content}")
        return None

def retrieve_scan_results(scan_id):
    time.sleep(30)  # URLScan.io may require a delay before results are ready
    results_response = requests.get(f"{RESULT_URL}/{scan_id}", headers=HEADERS)
    if results_response.status_code == 200:
        return results_response.json()
    else:
        print(f"Error retrieving results for scan {scan_id}: {results_response.content}")
        return None

def monitor_domains(domains, output_file, phishing_file):
    for domain in domains:
        scan_id = submit_to_urlscan(domain)
        if scan_id:
            results = retrieve_scan_results(scan_id)
            if results:
                # Process the results
                # Check if the domain is up and if there are any phishing indicators
                # For simplicity, we're just printing the results here
                print(f"Results for {domain}: {results}")
                log_to_file(output_file, f"Results for {domain}: {results}")

                # If you have specific indicators to check in the results, do it here
                # If phishing is detected:
                phishing_message = f'Phishing indicator detected on the domain: {domain}'
                print(phishing_message)
                log_to_file(phishing_file, phishing_message)

            # Sleep to avoid hitting URLScan.io rate limits
            time.sleep(15)

entities = read_lines_from_file('entities.txt')
domain_formats = read_lines_from_file('domains_formats.txt')
specific_indicators = read_lines_from_file('indicators.txt')

domains = [format.replace('*', entity) for entity in entities for format in domain_formats]

output_file = 'output.txt'
phishing_file = 'phishing_kit_hosted.txt'

monitor_domains(domains, output_file, phishing_file)
