from telebot import types

global width

width = 10

startButton = types.InlineKeyboardMarkup(row_width=8)
startButton.add(types.InlineKeyboardButton("Я деб", callback_data='start'))

chooseTrump = types.InlineKeyboardMarkup(row_width=8)
chooseTrump.add(
    *[
        types.InlineKeyboardButton(
            " " * 8 + ["♥️", "♦️", "♣️", "♠️"][i] + " " * 8,
            callback_data=f't{i}') for i in range(4)
    ]
)


def insert(text, word):
    return text[:len(text) // 2] + word + text[len(text) // 2:]


def makeText(card):
    s = card.name + card.suitPic
    if len(s) % 2:
        s = " " + s
    if card.state == 3:
        return "_" * width

    r = ""
    if card.checked:
        r = insert(r, "||")
    if card.state == 1:
        r = insert(r, "++")
    if card.state == 2:
        r = insert(r, "--")

    r = insert(r, "  " * (width - len(r + s)))
    return insert(r, s)


def drawTable(game):
    table = types.InlineKeyboardMarkup(row_width=8)
    for j in range(9):
        row = []
        for i in range(4):
            card = game.cards[i][j]
            row.append(types.InlineKeyboardButton(
                makeText(card),
                callback_data=f'c{i}{j}'
            ))
        table.add(*row)
    table.add(
        types.InlineKeyboardButton(insert(" " * width, "🏹"), callback_data='restart'),
        types.InlineKeyboardButton(insert(" " * width, "↑"), callback_data='opTake'),
        types.InlineKeyboardButton(insert(" " * width, "↓"), callback_data='meTake'),
        types.InlineKeyboardButton(insert(" " * width, "→"), callback_data='discard')
    )
    return table
