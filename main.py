from CardScraper import CardScraper


if __name__ == "__main__":
    main_url = "https://lil-alchemist.fandom.com/wiki/Category:Gold?from=A"
    card_scraper = CardScraper(main_url)
    class_elements = card_scraper.search_class()
    card_names = card_scraper.get_card_names(class_elements)
    base_link = "https://lil-alchemist.fandom.com/wiki/"
    fusion_types = card_scraper.get_card_info(card_names, base_link)

    for key in fusion_types:
        print(key)

    #myDict = {'Alien_Intruders': ('CriticalStrike', '8', '8'), 'Alien_Band': ('Absorb', '10', '6'), 'AL_9001': ('CriticalStrike', '8', '7'), 'Apocalypse': ('Orb', '9', '0'), 'Anger': ('Orb', '9', '0'), 'Ariel_(Card)': ('CriticalStrike', '12', '8'), 'Angel_Kid': ('CriticalStrike', '10', '5'), 'Angelfish': ('Protection', '4', '12'), 'Alien_Human_Hybrid': ('Absorb', '12', '5'), 'Asteroid_Prince': ('Protection', '7', '13'), 'Air_Sprite': ('CriticalStrike', '7', '10'), 'Avery_(Card)': ('Absorb', '12', '7'), 'Alien_Sorceress': ('Curse', '16', '4'), 'Arcade': ('Orb', '4', '5'), 'Auto_Champion': ('Protection', '5', '10'), 'Astronaut': ('Protection', '8', '8'), 'Angel_of_Wrath': ('Curse', '12', '3'), 'Amazing_Dog': ('Protection', '9', '10'), 'Assassin': ('Pierce', '15', '0'), 'Ares': ('CriticalStrike', '15', '2'), 'Angry_Mob': ('Crushing Blow', '10', '9'), 'Aurora': ('Absorb', '12', '5'), 'Aviator_Chin': ('Siphon', '9', '7'), 'Arm_Parasite': ('Protection', '8', '11'), 'Arch_Mage': ('Reflect', '14', '5'), 'Animal_Whisperer': ('Protection', '0', '15'), 'Ancient_Ark': ('Curse', '8', '8'), 'Alien_Reptile': ('Absorb', '15', '3'), 'Angel_Food_Cake': ('Absorb', '11', '4'), 'Avalanche': ('Crushing Blow', '16', '4'), 'Angel_of_Wisdom': ('Reflect', '8', '12'), 'Angel_Trumpeter': ('Protection', '6', '10'), 'Angelic_Mutant': ('CriticalStrike', '15', '5'), 'Absolute_Zero': ('CriticalStrike', '13', '7'), 'Atlas': ('Protection', '3', '13'), 'Affliction': ('Orb', '8', '1'), 'Ape_Lost_City': ('Protection', '4', '11'), 'Arcane_Golem': ('Amplify', '9', '5'), 'Alpha': ('CriticalStrike', '14', '4'), 'Arch_Angel': ('Block', '9', '9'), 'Angry_Bride': ('Protection', '13', '7')}
    