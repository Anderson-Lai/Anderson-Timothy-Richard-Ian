from modifications.getting.PRIVATE_get_modifications import PRIVATE_get_modifications

def get_upgrades() -> dict[str, bool]:
    
    settings = PRIVATE_get_modifications()

    del settings["coins"]

    return settings