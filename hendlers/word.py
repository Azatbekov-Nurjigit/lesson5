import aioschedule
from aiogram import types, Dispatcher
from coin import bot
import asyncio

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await message.answer("Ладно буду напоминать!")
async def spi():
    await bot.send_message(chat_id, text="Повторяй!")


async def word():
    aioschedule.every().wednesday.at("10:00").do(spi)
    aioschedule.every().saturday.at("10:00").do(spi)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)

def register_handlers_word(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'пуск' in word.text)

# import schedule
# import time
#
# def night():
#     print("СПАТЬ!!!")
#
# schedule.every().day.at("1:00").do(night)
# schedule.every().day.at("1:05").do(night)
# schedule.every().day.at("1:10").do(night)
# schedule.every().day.at("1:15").do(night)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)