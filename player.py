from functools import total_ordering


class player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.total_games = 0
    def print_player(self):
        print("Player: " + self.name + ". Symbol: " + self.symbol + " . Wins to total games: " + str(self.wins) + "/" + str(self.total_games))
    def won(self):
        self.wins += 1
        self.total_games += 1
    def lost(self):
        self.total_games += 1
    def winrate(self):
        if self.total_games == 0:
            return "0 games played."
        else:
            return str(self.wins / self.total_games * 100)
