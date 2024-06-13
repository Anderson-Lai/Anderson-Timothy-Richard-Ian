import json
from modifications.getting.get_modifications import get_modifications

def change_upgrade(upgrade: str, state: bool) -> None:
    state = get_modifications()
    state[upgrade] = state

    with open("./jsonFiles/modifications.json") as file:
        json.dump(state, file)