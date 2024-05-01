from aiogram.fsm.state import State, StatesGroup


class ApiToken(StatesGroup):
    token = State()
