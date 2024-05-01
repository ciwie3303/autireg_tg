from aiogram.filters import CommandStart
from aiogram.types import Message
from loader import *
from utils import *


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(f'''
Привет, <b>{message.from_user.full_name}!</b> 

Это панель управления <b>проектом.</b>''', reply_markup=await start_keyboard())

