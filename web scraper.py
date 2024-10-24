import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    
    response = requests.get(url)
    
    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        
        links = []
        for a_tag in soup.find_all('a', href=True):
            links.append(a_tag['href'])
        
        return links
    else:
        print(f"Failed to retrieve the page: {response.status_code}")
        return []

if __name__ == "__main__":
    
    url = 'https://example.com'  # Replace with the target URL
    links = scrape_site(url)
    
    
    for link in links:
        print(link)
