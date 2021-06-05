import json

from aiogram import types
from loguru import logger


def msgToLog(msg: types.Message, indent: int = None):
    logger.debug(json.dumps(json.loads(msg.__str__()), indent=indent))


def getLocale(msg: types.Message) -> str:
    if msg.from_user.locale == "ru":
        return "ru"
    elif msg.from_user.locale == "en":
        return "en"
    else:
        "ru"
