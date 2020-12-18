import telebot
import pandas as pd
import numpy as np
from telebot import types
frame = pd.read_excel('kachan.xls')
M = np.array(frame)
Token = "1408547637:AAFj2v_UNMSAN98zi26Hbyr74hAdhaVFiMY"
bot = telebot.TeleBot(Token)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('I')
    item2 = types.KeyboardButton('II')
    item3 = types.KeyboardButton('III')
    item4 = types.KeyboardButton('IV')
    item5 = types.KeyboardButton('V')
    item6 = types.KeyboardButton('VI')
    item7 = types.KeyboardButton('VII')
    item8 = types.KeyboardButton('VIII')

    markup.add(item1, item2, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id,
                     """"Hello, hello, меня зовут Cabbagehead, я был создан для того, чтобы помогать студентам быстро находить качественные реакции на определенные ионы в неорганической химии. 
    Алгоритм работы крайне прост: изначально, необходимо выбрать элемент из таблицы Менделеева, качественную реакцию на ион которого, тебе, fellow, хотелось бы узнать. Если такой элемент есть в моей программе, то тебе будет предложен ряд ионов, из которых необходимо выбрать нужный тебе. Далее, выбрав ион элемента, переходим к выбору конкретной качетсвенной реакции. 
    Бот выдает краткую справочную информацию о реакции, при необходимости каких-либо полезных комментариев, а также саму реакцию, цвет осадка и его фотографию. Для того, чтобы начать, напиши /start""",
                     parse_mode='html')
    bot.send_message(message.chat.id, 'Выбери номер группы: ', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def initialization_stage(message):
    if message.chat.type == 'private':
        if message.text == 'I':
            markup = types.InlineKeyboardMarkup(row_width=3)
            item1 = types.InlineKeyboardButton("Li", callback_data='Li')
            item2 = types.InlineKeyboardButton("Na", callback_data='Na')
            item3 = types.InlineKeyboardButton("K", callback_data='K')
            item4 = types.InlineKeyboardButton("Cu", callback_data='Cu')
            item5 = types.InlineKeyboardButton("Ag", callback_data='Ag')
            markup.add(item1, item2, item3,item4,item5)
            bot.send_message(message.chat.id, 'Выбери элемент ', reply_markup=markup)
        elif message.text == 'II':
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton('Ba', callback_data='Ba')
            item2 = types.InlineKeyboardButton('Ca', callback_data='Ca')
            item3 = types.InlineKeyboardButton('Mg', callback_data='Mg')
            item4 = types.InlineKeyboardButton('Sr', callback_data='Sr')
            item5 = types.InlineKeyboardButton('Zn', callback_data='Zn')
            item6 = types.InlineKeyboardButton('Hg', callback_data='Hg')
            markup.add(item1, item2, item3, item4, item5, item6)
            bot.send_message(message.chat.id, 'Выбери элемент ', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    elem = call.data
    c = np.where(elem == M)[0][0]
    bot.send_message(call.message.chat.id, frame.iloc[c][2])


bot.polling(none_stop=True)
