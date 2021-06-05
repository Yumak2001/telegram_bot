"""
Этот файл содержит слушатели на команды в боте
"""

from aiogram import types
from aiogram.types import BotCommand
from aiogram.utils import markdown as fmt
from loguru import logger

from app.misc import dp, i18n, bot
from app.utils.message import msgToLog, getLocale

_ = i18n.gettext


async def set_commands():
    commands = [
        BotCommand(command="/start", description="Старт"),
        BotCommand(command="/help", description="Справка")
    ]
    await bot.set_my_commands(commands)
    logger.info("Set my commands...")


@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    msgToLog(msg)
    await msg.answer(
        text=_(
            "Привет {user}\!",
            locale=getLocale(msg)
        ).format(
            user=fmt.bold(fmt.quote_html(msg.from_user.full_name)),
        )
    )


@dp.message_handler(commands=['help'])
async def process_start_command(msg: types.Message):
    msgToLog(msg)
    await msg.reply(
        text=_(
            "Это /help, есть команда /start",
            locale=getLocale(msg)
        )
    )
