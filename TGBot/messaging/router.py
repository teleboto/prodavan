
from telebot import types
from .action import Action

class Router:

  def __init__(self):
    self.routes = dict()

  def add_route(self, action_type, handler):
    self.routes[action_type] = handler

  def set_bot(self, bot):
    self.bot = bot

  def handle_message(self, callback: types.CallbackQuery, data: dict):
    action: Action = Action.from_dict(data)
    if action.type in self.routes and self.bot != None:
      self.routes[action.type](self.bot, callback)
