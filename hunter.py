import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout
import time

# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

def read_lines_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]

def log_to_file(file_path, text):
    with open(file_path, 'a') as file:
        file.write(text + "\n")

def check_for_indicators(url, indicators):
    try:
        response = requests.get(url, timeout=5, headers={'User-Agent': USER_AGENT})
        page_content = response.text.lower()
        for indicator in indicators:
            if indicator.lower() in page_content:
                return True
        return False
    except RequestException as e:
        print(RED + f"An error occurred for {url}: {e}" + ENDC)
        return False

def monitor_domains(domains, indicators, output_file, phishing_file):
    hosted_domains = set()
    phishing_domains = set()

    while True:
        for domain in domains:
            if domain in hosted_domains or domain in phishing_domains:
                continue  # Skip the check if domain is already logged

            url = f'https://{domain}'
            try:
                response = requests.get(url, timeout=5, headers={'User-Agent': USER_AGENT})
                
                if response.status_code == 200:
                    if domain not in hosted_domains:
                        hosted_message = f'Website hosted on the domain: {domain}'
                        print(GREEN + hosted_message + ENDC)
                        log_to_file(output_file, hosted_message)
                        hosted_domains.add(domain)

                    if domain not in phishing_domains and check_for_indicators(url, indicators):
                        phishing_message = f'Phishing indicator detected on the domain: {domain}'
                        print(GREEN + phishing_message + ENDC)
                        log_to_file(phishing_file, phishing_message)
                        phishing_domains.add(domain)
                
                else:
                    print(RED + f'{domain} returned status code: {response.status_code}' + ENDC)

            except ConnectionError:
                print(RED + f"{domain} could not be reached." + ENDC)
            except Timeout:
                print(RED + f"{domain} request timed out." + ENDC)
            except HTTPError as e:
                print(RED + f"HTTP error for {domain}: {e}" + ENDC)
            except Exception as e:
                print(RED + f'An unexpected error occurred for domain {domain}: {e}' + ENDC)

            time.sleep(1)

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/90.0.4430.212'
entities = read_lines_from_file('entities.txt')
domain_formats = read_lines_from_file('domains_formats.txt')
specific_indicators = read_lines_from_file('indicators.txt')

domains = [format.replace('*', entity) for entity in entities for format in domain_formats]

output_file = 'output.txt'
phishing_file = 'phishing_kit_hosted.txt'

monitor_domains(domains, specific_indicators, output_file, phishing_file)
