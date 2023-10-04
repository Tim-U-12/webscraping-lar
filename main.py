from CardScraper import CardScraper


if __name__ == "__main__":
    main_url = "https://lil-alchemist.fandom.com/wiki/Category:Gold?from=A"
    card_scraper = CardScraper(main_url)
    class_elements = card_scraper.search_class()
    card_names = card_scraper.get_card_names(class_elements)
    base_link = "https://lil-alchemist.fandom.com/wiki/"
    fusion_types = card_scraper.get_card_info(card_names, base_link)

    #print(fusion_types)
    