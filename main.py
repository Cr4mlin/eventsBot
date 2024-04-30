import telebot
import db
from telebot import types
import re
from datetime import datetime

token = '6735334749:AAEgtyEKVTYdJEBxsIR8KXXnbRGuHEYZ2wQ'
bot = telebot.TeleBot(token)

# Регулярное выражение для проверки формата даты и времени
date_time_pattern = re.compile(r'^(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}) (.*)$')

l = 8


@bot.message_handler(content_types=['text'])
def text(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    item1 = types.InlineKeyboardButton('Добавить', callback_data='add')
    item2 = types.InlineKeyboardButton('Удалить', callback_data='del')
    item3 = types.InlineKeyboardButton('Посмотреть', callback_data='view')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Выбери, действие', reply_markup=markup)


def add(message):
    match = date_time_pattern.match(message.text)
    if match:
        bot.send_message(message.chat.id, 'Сделано!')
        spisok = str(message.text).split()
        print(spisok[2])
        db.add_event(us, spisok[0], spisok[1], spisok[2])
    else:
        bot.send_message(message.chat.id,
                         'Формат ввода неправильный, попробуйте написать так - 1.05.2024 7:30 пробуждение')


# def delete(message):
#     try:
#         number = int(message.text)
#         b = db.view_event(us)
#         b = sorted(b, key=lambda x: datetime.strptime(x['date'] + ' ' + x['time'], '%d.%m.%Y %H:%M'))
#         e = b[number - 1]['event']
#         d = b[number - 1]['date']
#         t = b[number - 1]['time']
#         db.del_event(us, e, d, t)
#     except ValueError:
#         bot.send_message(message.chat.id, 'Пожалуйста, введите число')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global ci, mi, us
    us = call.message.chat.username
    ci = call.message.chat.id
    mi = call.message.id
    if call.message:
        if call.data == 'add':
            msg = bot.edit_message_text(chat_id=ci, message_id=mi,
                                        text='Напиши дату, время и действие в виде: "ДД.ММ.ГГГГ ЧЧ:ММ Действие"')
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
        elif call.data == 'del' or call.data == 'next':
            b = db.view_event(us)
            # Сортировка по времени
            b = sorted(b, key=lambda x: datetime.strptime(x['date'] + ' ' + x['time'], '%d.%m.%Y %H:%M'))
            for elem in b:
                markup1 = types.InlineKeyboardMarkup(row_width=len(b) + 1 if len(b) <= l else l)
                if len(b) <= l:
                    c = 1
                elif len(b) // l != 0 and len(b) % l != 0:
                    c = len(b) // l + 1
                else:
                    c = len(b) // l
                for i in range(c):
                    for elem in b:
                        a = elem['date'], elem['time'], elem['event']
                        markup1.add(types.InlineKeyboardButton(' -- '.join(a), callback_data=' '.join(a)))

            bot.edit_message_text(chat_id=ci, message_id=mi,
                                  text='Список ваших событий:\n', reply_markup=markup1)
        elif 'yes' in call.data:
            h = str(call.data)[4::].split(' -- ')
            e = h[2]
            t = h[1]
            d = h[0]
            print(h)
            print(d)
            db.del_event(us, e, d, t)
            bot.edit_message_text(chat_id=ci, message_id=mi, text=f'Сделано')
        elif call.data == 'no':
            msg = bot.send_message(call.message.chat.id, 'Хорошо')
            bot.register_next_step_handler(msg, text)
        else:
            a = str(call.data).split()
            h = ' -- '.join(a)
            choice = types.InlineKeyboardMarkup(row_width=2)
            yes = types.InlineKeyboardButton('Да', callback_data=f'yes {h}')
            no = types.InlineKeyboardButton('Нет', callback_data='no')
            choice.add(yes, no)
            bot.edit_message_text(chat_id=ci, message_id=mi,
                                  text=f'Вы точно хотите удалить событие:\n {h}?', reply_markup=choice)


bot.polling()
