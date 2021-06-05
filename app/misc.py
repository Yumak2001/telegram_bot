from pathlib import Path

from aiogram import Bot, Dispatcher, types
from loguru import logger

from app import config
from app.middlewares.i18n import I18nMiddleware

app_dir: Path = Path(__file__).parent.parent
locales_dir = app_dir / "locales"

bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.MARKDOWN_V2)
dp = Dispatcher(bot)
i18n = I18nMiddleware("bot", locales_dir, default="ru")


def setup():
    logger.info("Configure handlers...")

    import app.handlers

    from app.utils import executor
    from app import middlewares

    middlewares.setup(dp)
    executor.setup(True)

