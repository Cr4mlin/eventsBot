import telebot
import db
from telebot import types

token = '6735334749:AAEgtyEKVTYdJEBxsIR8KXXnbRGuHEYZ2wQ'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Добавить')
    item2 = types.KeyboardButton('Удалить')
    item3 = types.KeyboardButton('Посмотреть')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери, действие', reply_markup=markup)
@bot.message_handler(content_types='text')
def main(message):
    if message.text == 'Добавить':
        bot.send_message(message.chat.id, 'Напишите дату, время, событие')

@bot.message_handler(content_types='text')
def add_e(message):
    date, time, event = message.text.split
    db.add_event(message.chat.id, date, time, event)

bot.infinity_polling()