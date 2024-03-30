from telebot import TeleBot, custom_filters

from telebot.storage import StateMemoryStorage

from database.data_register import DataBase

from config import TOKIN

bot = TeleBot(TOKIN, state_storage=StateMemoryStorage())

db = DataBase()

bot.add_custom_filter(custom_filters.StateFilter(bot))