# Copyright (c) 2022 Itz-fork

import os


class Config(object):
    APP_ID = int(os.environ.get("APP_ID", 28853667))
    API_HASH = os.environ.get("API_HASH", "e20d060e00bb0b1f9645573e4f95207e")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6317945060:AAE8VqjA0HGWu23EtN4OBmGuPjMb7ttHZYI")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5841005593").split())
    IS_PUBLIC_BOT = os.environ.get("IS_PUBLIC_BOT") in ["True", "true"]
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL")) if os.environ.get("LOGS_CHANNEL") else None
    # DON'T CHANGE THESE 2 VARS
    DOWNLOAD_LOCATION = "./NexaBots"
    TG_MAX_SIZE = 2040108421
    # Mega User Account
    MEGA_EMAIL = os.environ.get("MEGA_EMAIL")
    MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD")