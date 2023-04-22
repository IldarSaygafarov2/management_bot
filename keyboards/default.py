from telebot import types

from utils import api


def show_registration_menu(chat_id=None):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        types.KeyboardButton(text="Регистрация")
    )
    return markup


def show_courses_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    courses: list[str] = [course["name"] for course in api.get_request_data(endpoint="courses")]
    buttons = [
        types.KeyboardButton(text=course.capitalize())
        for course in courses
    ]
    markup.add(*buttons)
    return markup


def show_teachers_menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    teachers: list[str] = [
        f"{teacher['first_name']} {teacher['last_name']}"
        for teacher in api.get_request_data(endpoint="teachers")
    ]
    buttons = [
        types.KeyboardButton(text=teacher)
        for teacher in teachers
    ]
    markup.add(*buttons)
    return markup

