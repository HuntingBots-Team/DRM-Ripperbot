import os
from config import Config

OWNER_ID = Config.OWNER_ID

# SUDO_USERS can be a comma-separated string of user IDs in env var, or a single int
sudo_env = Config.SUDO_USERS
if sudo_env:
    SUDO_USERS = [int(x.strip()) for x in str(sudo_env).split(",") if x.strip()]
else:
    SUDO_USERS = []

AUTHORIZED_GROUP_ID = Config.LOG_CHANNEL

def is_authorized(user_id: int, chat_id: int) -> bool:
    return user_id == OWNER_ID or user_id in SUDO_USERS or chat_id == AUTHORIZED_GROUP_ID
