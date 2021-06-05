from os import getenv

TELEGRAM_TOKEN = getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    exit("Error: no token provided")
