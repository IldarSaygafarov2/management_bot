from telebot import types

import messages
from data.loader import bot
from keyboards import default as kb


@bot.message_handler(func=lambda msg: msg.text == "Регистрация")
def handle_registration(message: types.Message):
    chat_id = message.from_user.id
    bot.send_message(chat_id, text=messages.USER_FIRST_NAME_MESSAGE)
    bot.register_next_step_handler(message, get_name)


def get_name(message: types.Message):
    chat_id = message.from_user.id
    first_name = message.text.title()
    bot.send_message(chat_id, text=messages.USER_LAST_NAME_MESSAGE)
    bot.register_next_step_handler(message, get_lastname, first_name)


def get_lastname(message: types.Message, first_name: str):
    chat_id = message.from_user.id
    last_name = message.text.title()
    bot.send_message(chat_id, text=messages.USER_COURSE_MESSAGE,
                     reply_markup=kb.show_courses_menu())
    bot.register_next_step_handler(message, get_course, first_name, last_name)


def get_course(message: types.Message, first_name: str, last_name: str):
    chat_id = message.from_user.id
    course = message.text
    bot.send_message(chat_id, text=messages.USERS_TEACHER_MESSAGE,
                     reply_markup=kb.show_teachers_menu())
    bot.register_next_step_handler(
        message, get_teacher, first_name, last_name, course)


def get_teacher(message: types.Message, first_name: str, last_name: str, course: str):
    chat_id = message.from_user.id
    teacher = message.text
    bot.send_message(chat_id,
                     text=messages.LESSON_DAYS_MESSAGE,
                     reply_markup=types.ReplyKeyboardRemove())
    bot.register_next_step_handler(
        message, get_lesson_days, first_name, last_name, course, teacher)


def get_lesson_days(message: types.Message, first_name: str, last_name: str, course: str, teacher: str):
    chat_id = message.from_user.id
    