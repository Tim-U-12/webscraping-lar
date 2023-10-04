from MainPage import CardScraper

# Example usage:
if __name__ == "__main__":
    main_url = "https://lil-alchemist.fandom.com/wiki/Category:Gold?from=A"
    card_scraper = CardScraper(main_url)
    class_elements = card_scraper.search_class()
    card_names = card_scraper.get_card_names(class_elements)
    base_link = "https://lil-alchemist.fandom.com/wiki/"
    fusion_types = card_scraper.get_fusion_types(card_names, base_link)

    print(fusion_types)
    #card_scraper.get_max_card_combat_stat(card_names)