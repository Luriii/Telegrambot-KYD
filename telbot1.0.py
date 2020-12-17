import telebot
import pandas as pd
import numpy as np
from telebot import types


frame = pd.read_excel('kachan.xls', header=0)
M = np.array(frame)
Token = '1302586780:AAH2QhIUyjPQCBVcIE3j7NMRNaVyvjle3m4'

bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('I')
    item2 = types.KeyboardButton('II')

    markup.add(item1, item2)

    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы обучить тебя химии.".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Выбери номер группы: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'I':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Li", callback_data='Li')
            item2 = types.InlineKeyboardButton("Na", callback_data='Na')
            item3 = types.InlineKeyboardButton("K", callback_data='K')
            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Выбери элемент ', reply_markup=markup)

        elif message.text == 'II':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Ba', callback_data='Ba')
            item2 = types.InlineKeyboardButton('Ca', callback_data='Ca')
            item3 = types.InlineKeyboardButton('Mg', callback_data='Mg')
            item4 = types.InlineKeyboardButton('Sr', callback_data='Sr')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'Выбери элемент ', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    elem = call.data
    c = np.where(elem == M)[0][0]
    bot.send_message(call.message.chat.id, frame.iloc[c][2])
    img = open(frame.iloc[c][3], 'rb')
    bot.send_photo(
        call.message.chat.id,
        photo=img)


# RUN
bot.polling(none_stop=True)
