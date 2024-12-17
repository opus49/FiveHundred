from hand import Hand

class Player:
    def __init__(self, index):
        self._index = index
        self._hand = Hand()

    @property
    def hand(self):
        return self._hand

    @property
    def index(self):
        return self._index

    def add_card(self, card):
        self._hand.add_card(card)

    def clear_hand(self):
        self._hand.clear()