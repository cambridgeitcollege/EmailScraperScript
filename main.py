import requests
import re
import sys
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

def get_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''

def get_emails(url, user_agent):
    try:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for bad status codes
        soup = BeautifulSoup(response.text, 'html.parser')
        # Improved regex for finding emails
        emails = set(re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", soup.text))
        return emails
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

def get_links(url, user_agent):
    try:
        headers = {'User-Agent': user_agent}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        for link in soup.find_all('a', href=True):
            links.add(link['href'])
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

def crawl_website(start_url, max_pages=20, user_agent='Mozilla/5.0'):
    domain_name = get_domain_name(start_url)
    if not domain_name:
        print('Invalid URL')
        return set()

    emails = set()
    links_to_visit = {start_url}
    visited_links = set()

    while links_to_visit and len(visited_links) < max_pages:
        url = links_to_visit.pop()
        if url in visited_links:
            continue

        visited_links.add(url)
        print(f"Crawling: {url}")

        # Only crawl pages within the same domain
        if get_domain_name(url) != domain_name:
            continue

        found_emails = get_emails(url, user_agent)
        if found_emails:
            emails.update(found_emails)
            print(f"Found {len(found_emails)} emails on {url}")

        found_links = get_links(url, user_agent)
        for link in found_links:
            absolute_link = urljoin(url, link)
            if absolute_link not in visited_links:
                links_to_visit.add(absolute_link)

    return emails

if __name__ == '__main__':
    start_url = input('Enter the URL: ')
    if not start_url.startswith(('http://', 'https://')):
        start_url = 'http://' + start_url

    # A simpler regex for basic URL validation
    if not re.match(r'https?://[^\s/$.?#].[^\s]*', start_url):
        print('Invalid URL format')
        sys.exit()

    emails = crawl_website(start_url)

    if emails:
        print('\n--- Found Emails ---')
        for email in sorted(list(emails)):
            print(email)
        print(f'\nTotal unique emails found: {len(emails)}')
    else:
        print('\nNo emails found.')
