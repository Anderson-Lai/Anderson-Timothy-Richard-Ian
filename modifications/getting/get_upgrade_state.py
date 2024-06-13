import json
from modifications.getting.get_modifications import get_modifications

def upgrade_state() -> dict[str, bool]:
    
    settings = get_modifications()

    del settings["coins"]
    del settings["shipColour"]

    return settings