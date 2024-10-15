# Email and Link Scraper

This Python script extracts emails and links from a given website URL. It crawls the domain for emails and retrieves all valid links on the web pages within the same domain.

## Features
- **Extract Emails**: Finds all email addresses from a webpage and other pages within the same domain.
- **Crawl Links**: Collects and follows all the links within the domain to continue email extraction.
- **Domain Validation**: The script checks if the provided URL is valid and belongs to the same domain before crawling.

## Prerequisites

Before running this script, ensure you have the following installed:

- **Python 3.x**
- **Requests**: To make HTTP requests.
- **BeautifulSoup (bs4)**: For parsing HTML content.
- **re**: For regular expression matching.

## Installation

- Clone this repository and install the required dependencies (if any):

```bash
git clone https://github.com/cambridgeitcollege/EmailScraperScript.git
cd EmailScraperScript
```
- Create the Virtual Environment (Not Necessary but Recommand) and activate it.
```bash
#For Linux User
python3 -m virtualenv venv
source venv/bin/activate
```

- Install the Requirements
```bash
pip install -r requirements.txt
```
- Run the `main.py` file


## Contributing
We welcome contributions! If you'd like to contribute to this Mero Share IPO Filler Script, please check out our [Contribution Guidelines](Contribution.md).

## Code of Conduct
Please review our [Code of Conduct](CodeOfConduct.md) before participating in this Script.
