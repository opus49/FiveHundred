from abc import ABC

class Pile(ABC):
    def __init__(self, cards=None):
        self._cards = cards if cards else []

    def add_card(self, card):
        self._cards.append(card)

    def clear(self):
        self._cards.clear()

    def pop_card(self):
        try:
            return self._cards.pop()
        except IndexError:
            return None

    def remove_card(self, card):
        self._cards.remove(card)

    def __len__(self):
        return len(self._cards)
    
    def __iter__(self):
        return iter(self._cards)

    def __str__(self):
        return "|".join(str(x) for x in self._cards)