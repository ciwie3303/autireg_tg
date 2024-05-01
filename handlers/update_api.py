from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.types import Message


@dp.callback_query(F.data == 'update_api')
async def status_project_handler(call: CallbackQuery, state: FSMContext):
    token = base.API_token
    await call.message.edit_text(f'<b>Токен сейчас:</b> <code>{token}</code>\n<b>Введите</b> новый <b>API токен:</b>',
                                 reply_markup=await back_keyboard())
    await state.set_state(ApiToken.token)


@dp.message(StateFilter(ApiToken.token))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(token=message.text)
    base.API_token = message.text
    base.save()
    await state.clear()
    await message.answer('<b>Токен</b> успешно изменён!', reply_markup=await start_keyboard())