import telebot
import os
from buttons import *
import buttons
from main import games
from game import Game

try:
    TOKEN = os.environ['TOKEN']
except:
    print("Токен пропал")
    TOKEN = ""

bot = telebot.TeleBot(TOKEN)


def update(id):
    bot.send_message(id, "Игрвой стол:",
                     reply_markup=drawTable(games[id]))


@bot.message_handler(commands=['start'])
def start(message):
    try:
        bot.send_message(message.chat.id, 'Сам ничерта не можешь, решил читы поискать?',
                         reply_markup=buttons.chooseTrump)
    except Exception as e:
        print(repr(e))


# Выбор козыря
@bot.callback_query_handler(func=lambda call: call.data[0] == "t")
def makeTable(call):
    try:
        id = call.message.chat.id
        games[id] = Game(int(call.data[1]), id)
        update(id)
    except Exception as e:
        print(repr(e))


# Выбор карты
@bot.callback_query_handler(func=lambda call: call.data[0] == "c")
def checkCard(call):
    try:
        id = call.message.chat.id
        games[id] \
            .cards[int(call.data[1])][int(call.data[2])] \
            .check()
        update(id)
    except Exception as e:
        print(repr(e))


# Сброс в бито:
@bot.callback_query_handler(func=lambda call: call.data == "discard")
def discard(call):
    try:
        id = call.message.chat.id
        games[id].check(3)
        update(id)
    except Exception as e:
        print(repr(e))


# Противник взял
@bot.callback_query_handler(func=lambda call: call.data == "opTake")
def opTake(call):
    try:
        id = call.message.chat.id
        games[id].check(2)
        update(id)
    except Exception as e:
        print(repr(e))


# Я взял
@bot.callback_query_handler(func=lambda call: call.data == "meTake")
def meTake(call):
    try:
        id = call.message.chat.id
        games[id].check(1)
        update(id)
    except Exception as e:
        print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data == "restart")
def restart(call):
    try:
        games.pop(call.message.chat.id)
    except Exception as e:
        print(repr(e))
    start(call.message)


print("Поехали")
bot.polling()
