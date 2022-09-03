import logging
import web_currency

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5521855231:AAFZVUm0JvtwF3aLjPzXytBfhV2p0vIengQ'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f'Hi, {message.from_user.username}!\nI\'m XYI7I-Bot!\nPowered by aiogram.')


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply(f'You can control me by sending these commands:\n'
                        f'/start - Hello!\n'
                        # f'Game\n'
                        # f'/game - challenge a game against the Bot\n'
                        f'Bot abilities\n'
                        f'/currency - currency rate calculator\n'
                        f'(currency from, currency to (def = RUB), amount (def = 1))')


@dp.message_handler(commands=['currency'])
async def send_currency(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    currency_calc = message.text.split()
    curr_fr = currency_calc[1]

    try:
        if len(currency_calc) == 3:
            amount = currency_calc[2]
            curr = web_currency.convert_currency_xe(curr_fr, amount=amount)
            await message.answer(f'{amount} {curr_fr} = {round(float(curr), 2)} RUB')
        else:
            curr = web_currency.convert_currency_xe(curr_fr)
            await message.answer(f'1 {curr_fr} = {round(float(curr), 2)} RUB')

    except:
        await message.answer(f'Выберите валюту:\n'
                             f'Доллары США - USD,\n'
                             f'Евро - EUR,\n'
                             f'Анлгийские фунты - GBP\n'
                             f'Японские иены - JPY\n'
                             f'Пример: /currency USD 10(по умолчанию = 1)')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
