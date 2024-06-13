import json
from modifications.getting.PRIVATE_get_modifications import PRIVATE_get_modifications

def change_upgrade(upgrade: str, state: bool) -> None:
    modifications = PRIVATE_get_modifications()
    modifications[upgrade] = state

    with open("./jsonFiles/modifications.json", "w") as file:
        json.dump(modifications, file)