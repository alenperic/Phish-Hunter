# Domain Monitoring Tool

## Overview
This Python script provides continuous monitoring of specified domains to detect active web hosting and the presence of potential phishing indicators. Once a domain is confirmed to host a website or a phishing indicator is detected, it is logged and will not be rechecked.

## Features
- Monitors a list of domains for active web hosting.
- Checks each domain for specific phishing indicators.
- Logs each domain only once to prevent redundant checks.
- Outputs hosted domains to `output.txt` and domains with phishing indicators to `phishing_kit_hosted.txt`.
- Color-coded console output for easy identification of issues and successful detections.

## Prerequisites
- Python 3.x
- `requests` library

## Usage

Before running the script, ensure `entities.txt`, `domains_formats.txt`, and `indicators.txt` are populated with the desired data.

To execute the script:

```bash
python hunter.py
```

## Files in the Repository
- `hunter.py`: The main Python script for domain monitoring.
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
