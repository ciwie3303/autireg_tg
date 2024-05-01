from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from loader import *


async def start_keyboard():
    builder = InlineKeyboardBuilder()
    if base.status == 0:
        builder.button(text='❌ Остановлен', callback_data='status_project')
    else:
        builder.button(text='✅ Запущен', callback_data='status_project')
    builder.button(text='Выгрузить сессии', callback_data='session_download')
    builder.button(text='Сменить API', callback_data='update_api')
    builder.button(text='Выгрузить логи', callback_data='download_logs')
    builder.adjust(1)
    return builder.as_markup()


async def back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='Назад', callback_data='back')
    builder.adjust(1)
    return builder.as_markup()

