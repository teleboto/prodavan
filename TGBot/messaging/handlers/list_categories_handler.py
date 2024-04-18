import telebot
from telebot import types
from db import categoryRepository
from messaging.action import Action

def list_categories_handler(bot: telebot.TeleBot, callback: types.CallbackQuery):
    data = categoryRepository.fetchAll()
    if len(data) > 0:
        markup = types.InlineKeyboardMarkup()
        for row in data:
            btn = types.InlineKeyboardButton(row["name"], callback_data=Action('list_goods', row["category_id"]).to_json())
            markup.row(btn)
        bot.send_message(callback.message.chat.id, "Вот что есть у меня,\nвыбирай чего нада", reply_markup=markup)
    else:
        bot.send_message(callback.message.chat.id, 'Прастити, но они раскупили все ваши товары (')
