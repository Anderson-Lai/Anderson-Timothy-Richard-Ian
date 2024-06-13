import json
from modifications.getting.PRIVATE_get_modifications import get_modifications

def change_upgrade(upgrade: str, state: bool) -> None:
    modifications = get_modifications()
    modifications[upgrade] = state

    with open("./jsonFiles/modifications.json", "w") as file:
        json.dump(modifications, file)