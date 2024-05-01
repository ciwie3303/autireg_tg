from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import types
from loader import *


from .api.api import get_countries


async def start_keyboard():
    builder = InlineKeyboardBuilder()
    if base.status == 0:
        builder.button(text='❌ Остановлен', callback_data='status_project')
    else:
        builder.button(text='✅ Запущен', callback_data='status_project')
    builder.button(text='Выгрузить сессии', callback_data='session_download')
    builder.button(text='Сменить API', callback_data='update_api')
    builder.button(text='Выбор страны', callback_data='country_')
    
    builder.button(text='Выгрузить логи', callback_data='download_logs')
    builder.adjust(2)
    return builder.as_markup()


async def countries_keyboard(api_key: str, page: int = 1):
    builder = InlineKeyboardBuilder()
    countries = await get_countries(api_key)

    if not countries:
        return None

    start_index = (page - 1) * 8
    end_index = min(start_index + 8, len(countries))
    
    for country_id, (country_name, _) in list(countries.items())[start_index:end_index]:
       
        builder.button(text=country_name, callback_data=f'countrys_{country_id}_{country_name}')
    
    total_pages = (len(countries) + 7) // 8  
    
    if page > 1:
        builder.button(text='Назад', callback_data=f'back_{page-1}')
    
    builder.button(text=f'{page}/{total_pages}', callback_data='dummy')
    
    if end_index < len(countries):
        builder.button(text='Вперед', callback_data=f'next_{page+1}')

    builder.adjust(2)
    return builder.as_markup()



async def back_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text='Назад', callback_data='back')
    builder.adjust(1)
    return builder.as_markup()

