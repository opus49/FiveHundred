from dataclasses import dataclass
from typing import Optional

FACE_CARDS = {10: "X", 11: "J", 12: "Q", 13: "K", 14: "A", 15: "*"}

@dataclass(frozen=True)
class Card:
    suit: Optional[str]
    rank: int

    def __str__(self):
        suit = self.suit[0].upper() if self.suit else "J"
        rank = FACE_CARDS.get(self.rank, self.rank)
        return f"{rank}{suit}"