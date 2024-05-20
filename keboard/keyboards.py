from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фото кота')
    button_2 = KeyboardButton('Перейти на 2 клавиатуру')
    button_3 = KeyboardButton('Перейти на 3 клавиатуру')
    keyboard.add(button_1, button_2, button_3)
    return keyboard

def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_4 = KeyboardButton('Отправь фото собаки')
    button_5 = KeyboardButton('Перейти на 1 клавиатуру')
    button_6 = KeyboardButton('Перейти на 3 клавиатуру')
    keyboard_2.add(button_4, button_5, button_6)
    return keyboard_2

def get_keyboard_3():
    keyboard_3 = ReplyKeyboardMarkup(resize_keyboard= True)
    button_7 = KeyboardButton('Отправь фото капибары')
    button_8 = KeyboardButton('Перейти на 1 клавиатуру')
    button_9 = KeyboardButton('Перейти на 2 клавиатуру')
    keyboard_3.add(button_7, button_8, button_9)
    return keyboard_3