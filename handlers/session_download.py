from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *
from aiogram.types import FSInputFile


@dp.callback_query(F.data == 'session_download')
async def download_sessions_handler(call: CallbackQuery):
    try:
        await create_rar()
        rar = FSInputFile("utils/sessions.rar", filename="sessions.rar")
        await call.message.answer_document(rar)
        await delete_rar()
    except:
        await call.message.answer('<b>Сессии отсутствуют.</b> Повторите попытку немного <b>позже.</b>')