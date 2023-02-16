from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btnBitcoin = InlineKeyboardButton(text='Bitcoin', callback_data='cc_bitcoin')
btnEthereum = InlineKeyboardButton(text='Ethereum', callback_data='cc_ethereum')
btnLitecoin = InlineKeyboardButton(text='Litecoin', callback_data='cc_litecoin')
btnMonero = InlineKeyboardButton(text='Monero', callback_data='cc_monero')
btnDash = InlineKeyboardButton(text='Dash', callback_data='cc_dash')

cripto_list = InlineKeyboardMarkup(row_width=1)
cripto_list.insert(btnBitcoin)
cripto_list.insert(btnEthereum)
cripto_list.insert(btnLitecoin)
cripto_list.insert(btnMonero)
cripto_list.insert(btnDash)
