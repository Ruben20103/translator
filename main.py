#Main.py

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


from logic import *

bot = telebot.TeleBot("7974971011:AAEZGKHDhWFH2Por9DR98N1xs8u-28xr0BI")

def gen_markup_for_text():
        markup = InlineKeyboardMarkup()
        markup.row_width = 1
        markup.add(InlineKeyboardButton('Получить ответ', callback_data='text_ans'),
                   InlineKeyboardButton('Перевести сообщение', callback_data='text_translate'))
        
        return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if "text" in call.data:
        obj = TextAnalysis.memory[call.from_user.username][-1]
        if call.data == "text_ans":
            bot.send_message(call.message.chat.id, obj.response)
        elif call.data == "text_translate":
            bot.send_message(call.message.chat.id,  obj.translation)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Дополнительное задание
    TextAnalysis(message.text, message.from_user.username)
    bot.send_message(message.chat.id, "Я получил твое сообщение! Что ты хочешь с ним сделать?", reply_markup=gen_markup_for_text())

bot.infinity_polling(none_stop=True)

#Logic.py

from translate import Translator
import requests
from collections import defaultdict

qwestions = {'Как тебя зовут' : "Я супер-крутой-бот и мое ппредназначение помогать тебе!",
             "Сколько тебе лет" : "Это слишком философский вопрос"}

class TextAnalysis():   
    
    memory = defaultdict(list)

    def __init__(self, text, owner):

        TextAnalysis.memory[owner].append(self)

        self.text = text
        self.translation = self.__translate(self.text, "ru", "en")

        if self.text in qwestions.keys():
            self.response = qwestions[self.text]
        else:
            self.response = self.get_answer() 

    
    def get_answer(self):
        res = self.__translate(self.__deep_pavlov_answer(), "en", "ru")
        return res

    def __translate(self, text, from_lang, to_lang):
        try:
            translator= Translator(from_lang=from_lang, to_lang=to_lang)
            translation = translator.translate(text)
            return translation
        except:
            return "Перевод не удался"

    def __deep_pavlov_answer(self):
        try:
            API_URL = "https://7038.deeppavlov.ai/model"
            data = {"question_raw": [ self.translation ]}
            res = requests.post(API_URL, json=data).json()
            res = res[0][0]
        except:
            res = "I don't know how to help"
        return res
