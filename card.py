class Card:
    def __init__(self, rank, suit, trump):
        self.rank = rank
        self.suit = suit
        self.trump = trump
        self.state = 0 # 0 in deck, 1 in my hand, 2 in opponent's hand, 3 in discard pile
        self.checked = False
        self.outDeck = False

        self.name = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"][rank]
        self.suitPic = ["♥️", "♦️", "♣️", "♠️"][suit]

    def check(self):
        self.checked = not self.checked
