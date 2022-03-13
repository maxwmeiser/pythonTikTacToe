from board import board
from player import player
import random

#this function checks than an input is either 1,2, or 3 and an integer
def check_in(input, lower, upper):
        try:
            if int(input) > lower and int(input) < upper:
                return True
            return False
        except:
            return False

class game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.board = board()

    def print_menu(self):
        print("placeholder")  

    def turn(self, rand):
        row_in = 0
        colm_in = 0
        #p1 first
        if rand:
            print("It's " + self.p1.name + "'s turn!")
            #attempt counter
            a = 0
            #while move doesnt return true. when exits while, move has been made
            while not self.board.move(self.p1, int(row_in), int(colm_in)):
                if a > 0:
                    print("Cannot play there! Try again.")
                
                row_in = input("Enter the row in which you'd like to make your move: ")
                #print(type(row_in))
                #repeatedly asks for input until valid input given
                while not check_in(row_in,0,4):
                    row_in = input("Invalid input. Please re-enter either 1, 2, or 3: ")

                colm_in = input("Enter the column in which you'd like to make your move: ")
                #repeating for column
                while not check_in(colm_in,0,4):
                    colm_in = input("Invalid input. Please re-enter either 1, 2, or 3: ")
                
                a += 1
        #p2 first
        else:
            print("It's " + self.p2.name + "'s turn!")
            #attempt counter
            a = 0
            #while move doesnt return true. when exits while, move has been made
            while not self.board.move(self.p2, int(row_in), int(colm_in)):
                if a > 0:
                    print("Cannot play there! Try again.")
                
                row_in = input("Enter the row in which you'd like to make your move: ")
                #print(type(row_in))
                #repeatedly asks for input until valid input given
                while not check_in(row_in,0,4):
                    row_in = input("Invalid input. Please re-enter either 1, 2, or 3: ")

                colm_in = input("Enter the column in which you'd like to make your move: ")
                #repeating for column
                while not check_in(colm_in,0,4):
                    colm_in = input("Invalid input. Please re-enter either 1, 2, or 3: ")
                
                a += 1

    def game_driver(self):
        GO = True
        random.seed()
        rand = random.choice([True,False])
        print(rand)
        while GO:
            self.board.print_board()
            self.turn(rand)
            if self.board.check_win():
                #most recent play won
                if rand:
                    #rand == true means p1 won
                    self.board.print_board()
                    print(self.p1.name + " won!")
                    self.p1.won()
                    self.p2.lost()
                else:
                    self.board.print_board()
                    print(self.p2.name + " won!")
                    self.p2.won()
                    self.p1.lost()
                return
            elif self.board.check_draw():
                self.board.print_board()
                print("It's a draw!")
                self.p1.draw()
                self.p2.draw()
                return
            rand = not rand
            self.board.print_board()
            self.turn(rand)
            if self.board.check_win():
                #most recent play won
                if rand:
                    #rand == true means p1 won
                    self.board.print_board()
                    print(self.p1.name + " won!")
                    self.p1.won()
                    self.p2.lost()
                else:
                    self.board.print_board()
                    print(self.p2.name + " won!")
                    self.p2.won()
                    self.p1.lost()
                return
            elif self.board.check_draw():
                self.board.print_board()
                print("It's a draw!")
                self.p1.draw()
                self.p2.draw()
                return
            rand = not rand


    
            
            
