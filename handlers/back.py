from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext


@dp.callback_query(F.data == 'back', StateFilter('*'))
async def start_handler(call: CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.edit_text(f'Привет, <b>{call.from_user.full_name}!</b> Это панель управления <b>проектом.</b>',
                              reply_markup=await start_keyboard())