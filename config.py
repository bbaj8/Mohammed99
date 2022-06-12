## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgAC_pN8kmln80kEGbItfwnrAUfHQuIFP3-xp2zMtXmpkYY4Get1aRONcbAersZV7C-HEx_Uj8na6hfFN06hz1tLsSFOo2_45_wC8AnOlx7TcHhnqgVaq3Q0SkhINpM10pHWZYagiTkOyW-7sQWe5LwLHwM2iRSPTpyrCMVtVmsZ-_bxQWhU40FsO39C_aaOHmoVDzkWeMARwjK4DKRtLAnGgEndfQQFSi6mR3A1-k4zql5nh7yDTFHpNXu0Mol_dV4gwo3SdLYNzW5ea65Csx_zELGvz9lTm0nfVHf9AHI9sDoRyntQMSRKW0DkJEelIADQ8vsqt6U2_zaEsf-F66HyAAAAATLkklEA")
BOT_TOKEN = getenv("BOT_TOKEN", "5304272902:AAEy8pTOvuhCVcoxLw5obTnfmZao0sKIKvs")
BOT_NAME = getenv("BOT_NAME", "Umk")
API_ID = int(getenv("API_ID", "12429107"))
API_HASH = getenv("API_HASH", "2c1096dfd767dfdfab961bb2fffe6be3")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "QQQLO")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "YIUIBOT")
OWNER_ID = getenv("OWNER_ID", "5386549632")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "vvbub")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "R125R")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "QQQLO")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5386549632").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/466de30ee0f9383c8e09e.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/d70bb6fa92728763c671f.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
