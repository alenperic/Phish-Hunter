# Phish-Hunter
An automated Python tool for continuous monitoring of domain integrity, identifying active web hosting, and detecting potential phishing threats.

## Overview
This repository contains a Python script for monitoring domains to check for website hosting and potential phishing indicators. The script is designed to be run continuously and logs information about each domain it monitors.

## Features
- Monitors domains for website hosting.
- Checks for specific phishing indicators on the webpages.
- Logs domains hosting websites to `output.txt`.
- Logs domains with detected phishing indicators to `phishing_kit_hosted.txt`.
- Simplified error logging for unreachable domains or request timeouts.

## Prerequisites
- Python 3
- `requests` library

## Usage

To run the script, use the following command:

```bash
python hunter.py
```

Ensure that `entities.txt`, `domains_formats.txt`, and `indicators.txt` are in the same directory as the script and contain the relevant data.

## Files
- `hunter.py`: The main script for domain monitoring.
- `entities.txt`: List of entities to monitor.
- `domains_formats.txt`: List of domain formats to check for each entity.
- `indicators.txt`: List of specific indicators that suggest a potential phishing attempt.
- `output.txt`: Log file for domains hosting a website.
- `phishing_kit_hosted.txt`: Log file for domains with detected phishing indicators.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
