import telebot
import db
from telebot import types

token = '6735334749:AAEgtyEKVTYdJEBxsIR8KXXnbRGuHEYZ2wQ'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Добавить', callback_data='add')
    item2 = types.InlineKeyboardButton('Удалить', callback_data='del')
    item3 = types.InlineKeyboardButton('Посмотреть', callback_data='view')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери, действие', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.message:
        if call.data == 'add':
            msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                  text='Напиши дату, время и действие')
            bot.register_next_step_handler(msg, add)

@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, 'Вы что-то хотели?')
def add(message):
    bot.send_message(message.chat.id, 'Сделано!')
    spisok = str(message.text).split()
    print(spisok[2])
    us = message.chat.username
    db.add_event(us, spisok[0], spisok[1], spisok[2])


bot.infinity_polling()
