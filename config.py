import os
import logging

# Corrected file paths with quotes
Credentials = 'auth/client_secrets.json'
TokenFile = 'auth/token.json'

# Configure logging
logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('log.txt'),
        logging.StreamHandler()
    ],
    level=logging.INFO
)

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1719450568:AAFs2Rtl1vroH0IBL91QFQuuBc5DYiX-M48")
    API_ID = int(os.environ.get("API_ID", 3975570))
    API_HASH = os.environ.get("API_HASH", "680b62f2844aa1954216f6cb99d2f3d9")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 2097152000
    TG_MAX_FILE_SIZE = 2097152000

    # Add your premium user session or skip (4GB)
    SESSION_STR = ""

    FREE_USER_MAX_FILE_SIZE = 2097152000
    MAX_SPLIT_SIZE = 4187407334
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "")
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    DEF_WATER_MARK_FILE = "@UploaderXNTBot"
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    # Duplicate DEF_WATER_MARK_FILE removed; kept only one

    # Properly handle optional environment variables for integers
    try:
        SUDO_USERS = [int(x) for x in os.environ.get("SUDO_USERS", "").split(',') if x]
    except ValueError:
        SUDO_USERS = []

    try:
        DRIVE_ID = int(os.environ.get("DRIVE_ID", ""))
    except ValueError:
        DRIVE_ID = None

    SESSION_NAME = os.environ.get(
        "SESSION_NAME",
        "AQA7eRMAdI8XLjuonz9nStZmtY1wJ05gCXoTGRTSe-S1pBCKayYbB8CtTZT1fhm9z0I0VU_YzFCJQbsUXUEudIA8MIwDFIUM9u68EP56oB7pvCLj1EV-4W9vKJR55ufa_qp4KqnCniV2mQ1vS98X9iwqe37j7IZ0F4K8fV2J8B-8VagJKKT_fOWyViJptWa3GFyem7X6qGXJ3KHdKCk_2RlMt48IEDwfRXeF8F1g5moxnsAlugP8SUvq7t7mVF5FcUFvWIqmGCBbPnsMKm-cCfyX6iNKPbtkpc23gmSKk8f0sLsT-y1zXQKKYMD0kElWxff3PaRnkLIQNL8QgdRNaJ32bch3yAAAAABNeVDBAA"
    )
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002676062227"))
    OWNER_ID = int(os.environ.get("OWNER_ID", 1606221784))
    LOGGER = logging
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002676062227")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@urltofile00bot")
