from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5901110505:AAFhE_U5iY-BW7dyUdo0gWemZfvI8-M67WA'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('Привет! Хочешь узнать свежую информацию о МТУСИ?')

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply('Я умею...')


@dp.message_handler(content_types=['text'])
async def send_welcome(message: types.Message):
    if message.text == 'хочу':
        await message.reply('Тогда тебе сюда - https://mtuci.ru/')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

