from telebot.handler_backends import State, StatesGroup


class RegisterState(StatesGroup):
    fullname = State()
    birthdate = State()
    contact = State()
    submit = State()


class CardState(StatesGroup):
    card = State()