import os
import urllib.parse
from dotenv import load_dotenv
import requests

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))

def search_recent_jobs():
    # Tailor this query to your exact target location & title preferences
    query = '"FastAPI" OR "Django" "Backend Engineer" intern OR junior site:greenhouse.io OR site:lever.co'
    
    # We use a standard duckduckgo HTML or text scraper to find URLs cleanly without expensive APIs
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            return []
        
        # Simple extraction of Lever and Greenhouse links from results
        import re
        links = re.findall(r'href="(https://boards\.greenhouse\.io/[^"]+|https://jobs\.lever\.co/[^"]+)"', response.text)
        
        # Deduplicate and return the top 3 freshest URLs found
        return list(set(links))[:3]
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []

if __name__ == "__main__":
    found_jobs = search_recent_jobs()
    # Print out results line by line for OpenClaw to process
    for job in found_jobs:
        print(job)