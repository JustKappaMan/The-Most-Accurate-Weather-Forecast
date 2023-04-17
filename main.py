import os
import logging

from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)

if (TOKEN := os.getenv('WEATHER_FORECASTER_TOKEN')) is None:
    raise ValueError('Error! Assign your Telegram bot token to WEATHER_FORECASTER_TOKEN system variable.')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi! I'm the most accurate weather forecaster on Telegram.")


@dp.message_handler(regexp='(?i)^saint[ -]petersburg$')
async def send_saint_petersburg_forecast(message: types.Message):
    await message.reply("It's raining in Saint-Petersburg, Russia. What else did you expect?")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
