from functools import total_ordering


class player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.losses = 0
        self.draws = 0
    def print_player(self):
        print("Player: " + self.name + ". Symbol: " + self.symbol + " . Record: " + self.wins + "-" + self.losses + "-" + self.draws)
    def won(self):
        self.wins += 1
    def lost(self):
        self.losses += 1
    def draw(self):
        self.draws += 1
    def winrate(self):
        return str(self.wins) + "-" + str(self.losses) + "-" + str(self.draws)
