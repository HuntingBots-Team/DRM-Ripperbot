from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

OWNER_ID = int(config.get("TELEGRAM", "OwnerID"))
SUDO_USERS = [int(x.strip()) for x in config.get("TELEGRAM", "SudoUsers").split(",") if x.strip()]

def is_authorized(user_id: int, chat_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS or chat_id == int(config.get("TELEGRAM", "AuthorizedGroupID"))
