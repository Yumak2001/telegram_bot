from aiogram import types
from aiogram.utils.exceptions import BotBlocked
from loguru import logger

from app.misc import dp


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    logger.info("{update}\nError: {exception}".format(update=update, exception=exception))
    return True
