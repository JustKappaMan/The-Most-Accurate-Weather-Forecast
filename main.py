import os
import logging

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

bot = Bot(token=os.getenv('WEATHER_FORECASTER_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm the most accurate weather forecaster on Telegram.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
