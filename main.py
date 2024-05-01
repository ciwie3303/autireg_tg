from handlers import *
from utils import *
import logging
from loader import *
import asyncio
import sys


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    print('Bot запущен успешно')
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename="py_log.log", filemode='w', format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(main())
