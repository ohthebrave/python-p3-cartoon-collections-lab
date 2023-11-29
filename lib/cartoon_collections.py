def roll_call_dwarves(arr):
    for index, dwarf in enumerate(arr, start=1):
        print(f'{index}. {dwarf}')

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]   

def summon_captain_planet(planeteer_calls):
    return [planet.capitalize() + '!' for planet in planeteer_calls]

short_words = ["two", "go", "industrious", "bop"]

def long_planeteer_calls(short_words):
    for word in short_words:
        if len(word) > 4:
            return True
    return False
    
snacks = ["crackers", "cheddar", "oyster crackers", "thyme"]

def find_the_cheese(snacks):
    cheese = ["cheddar", "gouda", "camembert"]

    for ingridient in snacks:
        if ingridient.lower() in cheese: 
            return ingridient
    return None