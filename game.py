from random import randint
from deck import Deck
from pile import Pile
from player import Player
from scorecard import Scorecard

class Game:
    def __init__(self):
        self.scorecard = Scorecard()
        self.deck = Deck()
        self.players = [Player(x) for x in range(0, 4)]
        self.widow = Pile()
        self.dealer_index = randint(0, 3)

    def deal_hand(self):
        self.dealer_index = (self.dealer_index + 1) % 4
        self.deck.reshuffle()
        print(f"Deck: {self.deck}")
        print(f"Dealer: {self.dealer_index}")
        self.widow.clear()
        for player in self.players:
            player.clear_hand()
            for _ in range(0, 10):
                player.add_card(self.deck.pop_card())
            print(f"Player {player.index}: {player.hand}")
        while len(self.deck) > 0:
            self.widow.add_card(self.deck.pop_card())
        print(f"Widow: {self.widow}")

    def play_game(self):
        while self.scorecard.winner is None:
            self.play_hand()
            break
        self.scorecard.print_results()
        
    def play_hand(self):
        print(f"Hand: {self.scorecard.hand_count + 1}")
        self.deal_hand()