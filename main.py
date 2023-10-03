import requests
from bs4 import BeautifulSoup

url = "https://lil-alchemist.fandom.com/wiki/Category:Gold"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    specific_class_elements = soup.findAll(class_='category-page__member-link')

    if specific_class_elements:
        # Loop through each element and print its text
        for element in specific_class_elements:
            print(f"Text inside element with specific class: {element}")
    else:
        print("Specified class not found in the page.")

else:
    print(f"Failed to retrieve the page: {response.status_code}")
    