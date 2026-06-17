import os
import urllib.parse
import re
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def search_recent_jobs():
    # Targets remote jobs referencing Python backend frameworks
    query = '"FastAPI" OR "Django" "Backend Engineer" intern OR junior site:greenhouse.io OR site:lever.co'
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return []
        
        # Scrape and extract direct ATS platform application pages cleanly
        links = re.findall(r'href="(https://boards\.greenhouse\.io/[^"]+|https://jobs\.lever\.co/[^"]+)"', response.text)
        
        # Deduplicate results and clean trailing URL escape characters
        cleaned_links = []
        for link in set(links):
            clean_link = link.split('&')[0].split('%')[0]
            if clean_link not in cleaned_links:
                cleaned_links.append(clean_link)
                
        # Limit to 3 fresh items to optimize context constraints on local models
        return cleaned_links[:3]
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

if __name__ == "__main__":
    found_jobs = search_recent_jobs()
    for job in found_jobs:
        print(job)
