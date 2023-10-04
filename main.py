import requests
from bs4 import BeautifulSoup

url = "https://lil-alchemist.fandom.com/wiki/Category:Gold"
response = requests.get(url)

if __name__ == "__main__":

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
     
        for link in soup.findAll('a',href=True):
            print(link['href'])

    else:
        print(f"Failed to retrieve the page: {response.status_code}")
        