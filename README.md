# Бот в телеграм «Напоминалка»

### Описание
Данный бот напоминает пользователю телеграмм о его указанных событиях. Бот взаимодействует с пользователем благодаря username. @N1234apominaniebot – юз бота в телеграм
### Управление
- Для управления бот используются удобные кнопки.
###Цель: Создать бота, который будет напоминать пользователю о его предстоящих событиях.

### Задачи бота:
1. Получать информацию от пользователя о запланированных событиях, таких как встречи, важные даты или задачи.
2. Сохранять эту информацию и устанавливать напоминания о предстоящих событиях.
3. Отправлять уведомления пользователю в удобное для него время, чтобы он не забыл о своих планах.
4. Давать пользователю возможность редактировать или удалять события из списка напоминаний.
5. Предлагать пользователю добавлять новые события или задачи для более эффективного управления своим временем.
6. Обладать интуитивным интерфейсом, чтобы пользователю было легко пользоваться ботом и настраивать его под себя.
###Методы и Технологии
import telebot
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
### Автор – Максим Панков, Игорь Черненко                                      
### Скриншоты бота ниже
![2024-05-07_08-13-28](https://github.com/Cr4mlin/eventsBot/assets/168114445/311c925d-9e12-4665-9065-e559a7b59c2c)
![2024-05-07_08-09-04](https://github.com/Cr4mlin/eventsBot/assets/168114445/0dc8a486-013c-4d79-8413-41581dffd986)
![2024-05-07_08-09-40](https://github.com/Cr4mlin/eventsBot/assets/168114445/52abe478-db44-43e2-8341-c23dcffbb031)

