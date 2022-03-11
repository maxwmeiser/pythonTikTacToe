from board import board
from player import player
from game import game

player1 = player("mate", "X")
player2 = player("lad2","O")
gamer = game(player1, player2)
gamer.game_driver()
player2.print_player()
player1.print_player()