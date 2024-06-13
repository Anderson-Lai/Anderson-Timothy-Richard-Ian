from modifications.getting.PRIVATE_get_modifications import get_modifications

def get_upgrades() -> dict[str, bool]:
    
    settings = get_modifications()

    del settings["coins"]
    del settings["shipColour"]

    return settings