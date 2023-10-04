import requests
from bs4 import BeautifulSoup

class MainPage():
    def __init__(self, url: str) -> None:
        self.url = url
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
             self.soup = BeautifulSoup(self.response.text, "html.parser")
        else:
            print(f"Failed to retrieve the page: {self.response.status_code}")
    
    def search_class(self, class_name="category-page__members") -> list:
        return self.soup.find_all(class_=class_name)

    def extract_links(self, container) -> list:
        links = []
        for element in container:
            for link in element.findAll('a',href=True):
                links.append(link['href'])
        return links


url = "https://lil-alchemist.fandom.com/wiki/Category:Gold"
x = MainPage(url)
class_name = x.search_class()
print(x.extract_links(class_name))