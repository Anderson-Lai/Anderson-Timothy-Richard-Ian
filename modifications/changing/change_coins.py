import json
from modifications.getting.get_coins import get_coins

def change_coins(amount: int) -> None:
    coins = get_coins()
    coins += amount
    
    if coins <= 0:
        coins = 0
    with open("./jsonFiles/modifications.json", "r") as file:
        settings = json.load(file)
        settings["coins"] = coins
    
    with open("./jsonFiles/modifications.json", "w") as file:
        json.dump(settings, file)
