import os
import logging
import pathlib

from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)

if (TOKEN := os.getenv('WEATHER_FORECAST_TOKEN')) is None:
    raise ValueError('Error! Assign your Telegram bot token to WEATHER_FORECAST_TOKEN system variable.')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm the most accurate weather forecaster on Telegram.")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("Just send me the name of the city and I'll provide you with up-to-date weather info.\n\n"
                         'Available cities:\n'
                         '1. Saint-Petersburg, Russia\n'
                         '2. Yakutsk, Russia\n'
                         '3. Philadelphia, United States',
                         '4. Atlantis')


@dp.message_handler(regexp='(?i)^saint[ -]petersburg$')
async def send_saint_petersburg_forecast(message: types.Message):
    with open(pathlib.Path('static', 'images', 'saint-petersburg.jpg'), 'rb') as photo:
        await message.reply_photo(photo, "🌧️ It's raining in Saint-Petersburg, Russia. What else did you expect?")


@dp.message_handler(regexp='(?i)^yakutsk$')
async def send_yakutsk_forecast(message: types.Message):
    with open(pathlib.Path('static', 'images', 'yakutsk.jpg'), 'rb') as photo:
        await message.reply_photo(photo,
                                  "❄️ It's freezing cold in Yakutsk, Russia. Don't forget your ushanka and valenki.")


@dp.message_handler(regexp='(?i)^(philadelphia|philly)$')
async def send_philadelphia_forecast(message: types.Message):
    with open(pathlib.Path('static', 'images', 'philadelphia.jpg'), 'rb') as photo:
        await message.reply_photo(photo, "☀️ It's sunny in Philadelphia, United States. As always.")


@dp.message_handler(regexp='(?i)^(atlantis|atlantida)$')
async def send_atlantis_forecast(message: types.Message):
    with open(pathlib.Path('static', 'images', 'atlantis.jpg'), 'rb') as photo:
        await message.reply_photo(photo, "🌊 Hmm. I'd recommend you get a diving suit on.")


@dp.message_handler(regexp='(?i)billy')
async def send_billy_easter_egg(message: types.Message):
    with open(pathlib.Path('static', 'sounds', 'billy.ogg'), 'rb') as sound:
        await message.reply_voice(sound, '🤬 Did you just mention <b>Billy</b>?!', parse_mode='HTML')


@dp.message_handler()
async def send_error(message: types.Message):
    await message.reply("I don't know anything about this place. Use /help to see the list of supported locations.")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
