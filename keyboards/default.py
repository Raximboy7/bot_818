from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton
from main import *

def register_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Ro'yxattan o'tish 👨‍💻")
               )
    return markup

def sent_contact():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton("Raqamni jo'natish 📱", request_contact=True))
    return markup


def main_menyu():
    markup  = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton('Asosiy Menyu 🏠'),
        KeyboardButton('About 🤖')
    )
    return markup

def yes_no():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Yes✔️"),
    KeyboardButton("No✖️")
    )
    return markup
def vidio_btn(doms:list):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for dom in doms:
        markup.add(KeyboardButton(dom[0]))
    markup.add( 'Main Menu 🔙')

