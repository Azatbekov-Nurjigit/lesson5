import asyncio
import logging
from aiogram.utils import executor
from coin import  dp
from handlers import client, callback, fsmAdminMentor, eztra, word

async def on_startup(_):
    asyncio.create_task(word.scheduler())
    sql_create()


client.register_handler_client(dp)
callback.register_handler_callback(dp)
fsmAdminMentor.register_handler_fsmAdminMentor(dp)
word.register_handlers_word(dp)
eztra.register_handler_ezta(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

# Создайте любое
# уведомление для себя
# которое
# будет отличаться от
# уведомления на уроке
# - Это уведомление
# должно
# приходить в особый
# день , не
# каждый день

