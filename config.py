import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = "5049507559:AAETCRZ2YM2VR9fj8DuNIfqUEnxp1HSavoc"

#Your API ID from my.telegram.org
APP_ID = 2919867

#Your API Hash from my.telegram.org
API_HASH = "90dd95178a8d13a69bfdbc7da68d23a4"

#Your db channel Id
CHANNEL_ID = -1001705686821

#OWNER ID
OWNER_ID = 1791795037

#Database 
DB_URI = "postgres://qfokcisu:w7kIyJJ4VmBuyCHAMaG-R32ifb-_2HE4@castor.db.elephantsql.com/qfokcisu"

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = -1001611440971

TG_BOT_WORKERS = 4

#start message
START_MSG = " Take files "

ADMINS=[5073412581,1392459364,1242979521,1337239251,2043468602]

#Force sub message 
FORCE_MSG = "Join channel and retry"
#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = None

USE_GROUP = None
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = True

ADMINS.append(OWNER_ID)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
