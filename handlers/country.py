from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *

@dp.callback_query(F.data == 'country_')
async def country_handler(call: CallbackQuery):
    token = base.API_token
    await call.message.edit_reply_markup(reply_markup=await countries_keyboard(token))

@dp.callback_query(F.data.startswith('countrys_'))
async def next_page_handler(call: CallbackQuery):
    country_id = call.data.split('_')[1]
    country_name = call.data.split('_')[2]

    with db.atomic():
        Settings.update(Country=country_id).execute()
        
    await call.message.edit_text(f'''
<b>Вы выбрали страну:</b> <i>{country_name}</i>

<b>После того как запустите авторегистртратор не советую менять страну. 
Остановите регистрирование, затем меняйте страну! </b>
''', reply_markup=await back_keyboard())

@dp.callback_query(F.data.startswith('next_'))
async def next_page_handler(call: CallbackQuery):
    token = base.API_token
    page = int(call.data.split('_')[1])
    await call.message.edit_reply_markup(reply_markup=await countries_keyboard(token, page))

@dp.callback_query(F.data.startswith('back_'))
async def back_page_handler(call: CallbackQuery):
    token = base.API_token
    page = int(call.data.split('_')[1])
    await call.message.edit_reply_markup(reply_markup=await countries_keyboard(token, page))