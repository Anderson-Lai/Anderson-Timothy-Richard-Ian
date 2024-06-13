import json

# this function should only be used in conjunctino with other functions
# never by itself

def get_modifications() -> dict:
    with open("./jsonFiles/modifications.json", "r") as file:
        return json.load(file)