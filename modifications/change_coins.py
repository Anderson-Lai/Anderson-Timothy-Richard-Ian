import json
from modifications.get_coins import get_coins

def change_coins(amount: int) -> None:
    coins = get_coins()
    coins += amount
    
    with open("./jsonFiles/modifcations.json", "r") as file:
        settings = json.load(file)
        settings["coins"] = coins
    
    with open("./jsonFiles/modifcations.json", "w") as file:
        json.dump(settings, file)