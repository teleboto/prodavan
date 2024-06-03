import telebot
from telebot import types
from db import cartRepository
from messaging.action import Action
from.show_cart_handler import show_cart_handler

def clear_cart_handler(bot: telebot.TeleBot, callback: types.CallbackQuery, action):
    user_id = callback.from_user.id
    cartRepository.clear(user_id)
    show_cart_handler(bot, callback, action)
