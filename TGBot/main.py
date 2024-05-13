import telebot
from telebot import types
import json

from config import config
from messaging.action import Action
from messaging import router

print("Бот запускается")

bot = telebot.TeleBot(config["TELEBOT_API_KEY"])
router.set_bot(bot)

@bot.message_handler(commands=['start'])
def main(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Акции и специальные предложения', callback_data='special')
    btn2 = types.InlineKeyboardButton('Каталог', callback_data=Action('catg', '').to_json())
    btn3 = types.InlineKeyboardButton('Корзина', callback_data='baskt')
    btn4 = types.InlineKeyboardButton('Статус заказа', callback_data='status')
    btn5 = types.InlineKeyboardButton('Помощь', callback_data='help')
    markup.row(btn1)
    markup.row(btn2, btn3)
    markup.row(btn4, btn5)
    file = open('./logo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup, caption = f'<b>👋 Привет {message.from_user.first_name}'\
    '\n 🛍 Добро пожаловать в бот магазина Prodavan</b>\n *описание магазина*', parse_mode='html')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Если у вас возникли вопросы, напишите нам')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'<b>👋 Привет {message.from_user.first_name}')
    if message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback: types.CallbackQuery):

    print(callback.from_user.id)

    data = None
    try:
        data = json.loads(callback.data)
    except:
        pass

    if data != None:
        router.handle_message(callback, data)
    else:
        if callback.data == 'baskt':
            bot.send_message(callback.message.chat.id, '*открывается корзина*')
        elif callback.data == 'status':
            bot.send_message(callback.message.chat.id, '*открывается статус заказа*')
        elif callback.data == 'help':
            bot.send_message(callback.message.chat.id, '*открывается помощь*')
        elif callback.data == 'special':
            bot.send_message(callback.message.chat.id, '*открываются спецпредложения*')

print("Бот работает")

bot.polling(none_stop=True)

print("\nБот завершает работу")
