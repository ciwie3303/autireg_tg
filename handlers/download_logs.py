from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *
from aiogram.types import FSInputFile


@dp.callback_query(F.data == 'download_logs')
async def download_sessions_handler(call: CallbackQuery):
    rar = FSInputFile("py_log.log", filename="logs.log")
    await call.message.answer_document(rar)
