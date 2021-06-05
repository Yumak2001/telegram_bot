from aiogram import types
from aiogram.utils import markdown as fmt

from app.misc import dp, i18n
from app.utils.message import msgToLog

_ = i18n.gettext


@dp.message_handler(content_types=[types.ContentType.DOCUMENT])
async def download_doc(msg: types.Message):
    msgToLog(msg)
    # Скачивание в каталог с ботом с созданием подкаталогов по типу файла
    await msg.document.download()
    await msg.reply(_("Это ответ на документ {fileName}").format(fileName=fmt.code(msg.document.file_name)))


# Типы содержимого тоже можно указывать по-разному.
@dp.message_handler(content_types=["photo"])
async def download_photo(msg: types.Message):
    msgToLog(msg)
    await msg.photo[-1].download()
    await msg.answer(_("Это ответ на фото"))
