import telebot
import db
from telebot import types
import re
from datetime import datetime

token = '6735334749:AAEgtyEKVTYdJEBxsIR8KXXnbRGuHEYZ2wQ'
bot = telebot.TeleBot(token)

# Регулярное выражение для проверки формата даты и времени
date_time_pattern = re.compile(r'^(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}) (.*)$')

@bot.message_handler(content_types=['text'])
def text(message):
    global us
    us = message.chat.username
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Добавить', callback_data='add')
    item2 = types.InlineKeyboardButton('Удалить', callback_data='del')
    item3 = types.InlineKeyboardButton('Посмотреть', callback_data='view')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери, действие', reply_markup=markup)

def add(message):
    match = date_time_pattern.match(message.text)
    if match:
        spisok = match.groups()
        if not db.check_event(us, spisok[0], spisok[1]):
            bot.send_message(message.chat.id, 'Сделано!')
            db.add_event(us, spisok[0], spisok[1])
        else:
            bot.send_message(message.chat.id, 'Такое событие уже существует.')
    else:
        bot.send_message(message.chat.id, 'Формат ввода неправильный, попробуйте написать так - 1.05.2024 7:30 пробуждение')

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global ci, mi
    ci = call.message.chat.id
    mi = call.message.id
    if call.message:
        if call.data == 'add':
            msg = bot.edit_message_text(chat_id=ci, message_id=mi,
                                        text='Напиши дату, время и действие')
            bot.register_next_step_handler(msg, add)
        elif call.data == 'view':
            b = db.view_event(us)
            # Сортировка по времени
            b = sorted(b, key=lambda x: datetime.strptime(x['date'] + ' ' + x['time'], '%d.%m.%Y %H:%M'))
            s = ''
            for elem in b:
                a = elem['date'], elem['time'], elem['event']
                s += ' -- '.join(a) + '\n'
            bot.edit_message_text(chat_id=ci, message_id=mi,
                                  text='Список ваших дел:\n' + s)

bot.infinity_polling()