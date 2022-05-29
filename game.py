from card import Card


class Game:
    def __init__(self, trump, id):
        self.id = id
        self.deck = 24
        self.trump = trump
        self.cards = \
            [[Card(j, i, trump == i) for j in range(9)] for i in range(4)]
        self.opponentHand = 6


    def check(self, x):
        for i in range(4):
            for j in range(9):
                if self.cards[i][j].checked:
                    self.cards[i][j].state = x
                    self.cards[i][j].checked = False
                    if not self.cards[i][j].outDeck:
                        self.deck -= 1
                    # if x == 3:

