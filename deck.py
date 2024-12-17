import random
from card import Card
from pile import Pile

SUITS = {
    "spades": 40,
    "clubs": 60,
    "diamonds": 80,
    "hearts": 100,
}

class Deck(Pile):
    def __init__(self):
        super().__init__(self._build_deck())

    @staticmethod
    def _build_deck():
        cards = [Card(suit=suit, rank=rank) for suit in SUITS.keys() for rank in range(4, 15)]
        cards.append(Card(suit=None, rank=15))
        return cards

    def fast_shuffle(self):
        random.shuffle(self._cards)

    def reshuffle(self):
        self._cards = self._build_deck()
        self.fast_shuffle()