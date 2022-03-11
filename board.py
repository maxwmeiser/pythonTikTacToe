from operator import truediv
from player import player

class board:
    def __init__(self):
        self.game_board = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"],
        ]
    
    #this function prints the 3 by 3 board
    def print_board(self):
        i = 0
        n = 0
        print("\n--Current board--")
        while i < 3:
            while n < 3:
                print("  " + self.game_board[i][n] + "  ", end = "")
                if n < 2:
                    print("|", end = "")
                n += 1
            print("\n")
            i += 1
            n = 0

    #this function allows the player to input a move. 
    #PARAM: player, row (1-3), column(1-3)
    def move(self, player, row, column):
        row -= 1
        column -= 1
        #checks the targeted row,column is in range and not already changed
        if self.game_board[row][column] != "-" or 0 > row or 0 > column or row > 2 or column >2:
            return False
        else:
            self.game_board[row][column] = player.symbol 
            return True

    #this function checks to see if a player has won
    def check_win(self):
        if self.game_board[0][0] == self.game_board[0][1] == self.game_board[0][2] and self.game_board[0][0] != "-":
            return True
        elif self.game_board[1][0] == self.game_board[1][1] == self.game_board[1][2] and self.game_board[1][0] != "-":
            return True
        elif self.game_board[2][0] == self.game_board[2][1] == self.game_board[2][2] and self.game_board[2][0] != "-":
            return True
        elif self.game_board[0][0] == self.game_board[1][0] == self.game_board[2][0] and self.game_board[0][0] != "-":
            return True
        elif self.game_board[0][1] == self.game_board[1][1] == self.game_board[2][1] and self.game_board[0][1] != "-":
            return True
        elif self.game_board[0][2] == self.game_board[1][2] == self.game_board[2][2] and self.game_board[0][2] != "-":
            return True
        elif self.game_board[0][0] == self.game_board[1][1] == self.game_board[2][2] and self.game_board[0][0] != "-":
            return True
        elif self.game_board[0][2] == self.game_board[1][1] == self.game_board[2][0] and self.game_board[0][2] != "-":
            return True
        else:
            return False

            