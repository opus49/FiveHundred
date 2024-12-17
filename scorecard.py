class Scorecard:
    def __init__(self):
        self._odds = 0
        self._evens = 0
        self._winner = None
        self._hand_count = 0

    @property
    def evens(self):
        return self._evens

    @property
    def hand_count(self):
        return self._hand_count

    @property
    def odds(self):
        return self._odds

    @property
    def winner(self):
        return self._winner

    def print_results(self):
        print(f"Winner: {self.winner}  Odds: {self.odds}  Evens: {self.evens}  Hands: {self.hand_count}")

    def update_score(self, odds, evens, dealer_index):
        self._hand_count += 1
        self._odds += odds
        self._evens += evens
        is_dealer_even = dealer_index % 2 == 0
        if self._odds <= -500 or (is_dealer_even and self.evens >= 500):
            self._winner = "evens"
        elif self._evens <= -500 or (not is_dealer_even and self.odds >= 500):
            self._winner = "odds"