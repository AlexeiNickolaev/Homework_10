from aiogram import Bot, Dispatcher, executor, types
from pycoingecko import CoinGeckoAPI
from buttons import cripto_list
from datetime import datetime

bot = Bot('Token')
dp = Dispatcher(bot)
cg = CoinGeckoAPI()


async def startUp(_):
    print('Бот запущен!')


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.chat.type == 'private':
        user_data = []
        user_data.append(datetime.now())
        user_data.append(message.from_user.full_name)
        user_data.append(message.from_user.id)
        user_data.append(message.from_user.username)
        user_data = list(map(str, user_data))
    with open('Bot\\log.txt', 'a', encoding='utf-8') as data:
        data.write(' | '.join(user_data) + '\n')
    await bot.send_message(message.from_user.id,  f'Привет, {message.from_user.first_name}!\nЯ показываю курс\
 криптовалют.\n Выбери криптовалюту', reply_markup=cripto_list)


@dp.callback_query_handler(text_contains='cc_')
async def cripto(call: types.CallbackQuery):
    await bot.delete_message(call.from_user.id, call.message.message_id)
    callback_data = call.data
    print(call.data)
    currency = str(callback_data[3:])
    result = cg.get_price(ids=currency, vs_currencies='usd')
    await bot.send_message(call.from_user.id, f'Криптовалюта: {currency}\nСтоимость на данный момент {result[currency]["usd"]}$', reply_markup=cripto_list)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=startUp)
