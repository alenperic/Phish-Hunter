# Phish Hunter
An automated Python tool for continuous monitoring of domain integrity, identifying active web hosting, and detecting potential phishing threats.

## Overview
Phish Hunter is a collection of Python scripts designed to automate the monitoring of domains for active web hosting and potential phishing threats. It includes two main scripts: `hunter.py` for general domain monitoring and `URLscan_hunter.py` for detailed analysis using the URLScan.io API.

## Features
- `hunter.py` continuously monitors domains, checks for phishing indicators, and logs findings.
- `URLscan_hunter.py` integrates with the URLScan.io API for an in-depth scan and analysis of each domain.
- Domains are checked only once, with results logged to prevent redundant checks.
- Color-coded console output for clear visibility of domain status.
- Logs are maintained for both hosted domains and detected phishing indicators.

## Prerequisites
- Python 3.x
- `requests` library

## Usage

Ensure `entities.txt`, `domains_formats.txt`, and `indicators.txt` are populated with the desired data before running the scripts.

To execute `hunter.py`:

```bash
python hunter.py
```

To execute `URLscan_hunter.py` (requires an API key from URLScan.io):

```bash
python URLscan_hunter.py
```

## Demo
![Demonstration GIF](https://github.com/alenperic/Phish-Hunter/blob/main/demo.gif?raw=true)

## Files in the Repository
- `hunter.py`: The main Python script for domain monitoring.
- `URLscan_hunter.py`: Uses URLScan.io's API to perform detailed scans of domains.
- `entities.txt`: Contains the entities (e.g., domain names) to be monitored.
- `domains_formats.txt`: Contains domain formats to be checked for each entity.
- `indicators.txt`: Contains specific indicators to detect potential phishing attempts.
- `output.txt`: Auto-generated log file for domains confirmed to host a website.
- `phishing_kit_hosted.txt`: Auto-generated log file for domains with detected phishing indicators.
- `requirements.txt`: Lists the Python dependencies required for the script.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your suggested changes.

## License
This project is released under the [MIT License](LICENSE).
