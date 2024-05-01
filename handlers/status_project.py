from aiogram import F
from aiogram.types import CallbackQuery
from loader import *
from utils import *


@dp.callback_query(F.data == 'status_project')
async def status_project_handler(call: CallbackQuery):
    if base.status == 0:
        base.status = 1
    else:
        base.status = 0

    base.save()
    await call.message.edit_reply_markup(reply_markup=await start_keyboard())


