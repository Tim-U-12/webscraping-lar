import re
import requests
from bs4 import BeautifulSoup

class CardScraper:
    def __init__(self, url: str) -> None:
        self.url = url
        self.soup = self._get_soup(self.url)
    
    def _get_soup(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            return BeautifulSoup(response.text, "html.parser")
        else:
            raise Exception(f"Failed to retrieve the page: {response.status_code}")

    def search_class(self, class_name="category-page__members") -> list:
        return self.soup.find_all(class_=class_name)

    def get_card_names(self, container) -> list:
        card_names = set()
        for element in container:
            for link in element.find_all('a', href=True):
                card_names.add(re.sub('/wiki/', '', link['href']))
        return list(card_names)

    def get_card_info(self, card_names, base_link):
        result = {}
        for card_name in card_names:
            attack = None
            defence = None
            fusiontype = None

            card_url = base_link + card_name
            soup = self._get_soup(card_url)

            a_tags = soup.find_all('a', title='Fusion')
            for a_tag in a_tags:
                img_tag = a_tag.find('img')
                if img_tag:
                    alt_value = img_tag.get('alt', None)
                    fusiontype = alt_value
            
            container = soup.find_all(class_="pi-horizontal-group-item")
            for elements in container:
                img_tag = elements.find('img')
                if img_tag and 'alt' in img_tag.attrs:
                    alt = img_tag['alt'].split(" ")[0]
                    if alt.lower() == 'attack':
                        attack = elements.text.replace(" ", "")
                    elif alt.lower() == 'defense':
                        defence = elements.text.replace(" ", "")

            result[card_name] = (fusiontype, attack, defence)
        return result
