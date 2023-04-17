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


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Just send me the name of the city and I'll provide you with up-to-date weather info.\n\n"
                        'Available cities:\n'
                        '1. Saint-Petersburg, Russia\n'
                        '2. Philadelphia, United States')


@dp.message_handler(regexp='(?i)^saint[ -]petersburg$')
async def send_saint_petersburg_forecast(message: types.Message):
    await message.reply("It's raining in Saint-Petersburg, Russia. What else did you expect?")


@dp.message_handler(regexp='(?i)^(philadelphia|philly)$')
async def send_philadelphia_forecast(message: types.Message):
    await message.reply("It's sunny in Philadelphia, United States. As always.")


@dp.message_handler()
async def send_error(message: types.Message):
    await message.reply("I don't know anything about this place. Use /help to see the list of supported locations.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
