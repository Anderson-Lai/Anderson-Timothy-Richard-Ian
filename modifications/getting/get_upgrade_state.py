from modifications.getting.get_upgrades import get_upgrades

def get_upgrade_state(upgrade: str) -> bool:

    settings = get_upgrades()
    return settings[upgrade]