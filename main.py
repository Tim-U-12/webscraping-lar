from CardScraper import CardScraper
import csv


if __name__ == "__main__":
    base_url = "https://lil-alchemist.fandom.com/wiki/Category:Gold?from="
    capital_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for letter in capital_letters:
        main_url = base_url + letter

        card_scraper = CardScraper(main_url)
        class_elements = card_scraper.search_class()
        card_names = card_scraper.get_card_names(class_elements)
        base_link = "https://lil-alchemist.fandom.com/wiki/"
        cards_info = card_scraper.get_card_info(card_names, base_link)

        file_path = "card_info.csv"
        with open(file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            for card_info in cards_info:
                csv_writer.writerow(card_info)
            
    csv_file.close()