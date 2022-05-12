import sys
import random
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

#TODO:
#Program breaks when blank input for symbol 
#Dont allow blank name profile 
#should use a dictionary to store player profiles
#when game window closed, game doesnt reset

#stores player profile data: name, symbol, W, L, D
class player_profile():
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.losses = 0
        self.draws = 0
    
    def won_game(self):
        self.wins += 1
    
    def draw_game(self):
        self.draws += 1

    def lost_game(self):
        self.losses += 1

class game_window(QDialog):
    def __init__(self):
        #setup
        super(game_window,self).__init__()
        loadUi('gamewindow.ui',self)
        #initialize gameboard representation
        self.gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
        #initialize players
        self.p1_name = ""
        self.p1_symbol = ""
        self.p2_name = ""
        self.p2_symbol = ""
        self.p1_turn = True
        self.label_Instructor.setText("Make your move by clicking a box...")
        #hiding labels
        self.label_r1c1.hide()
        self.label_r1c2.hide()
        self.label_r1c3.hide()
        self.label_r2c1.hide()
        self.label_r2c2.hide()
        self.label_r2c3.hide()
        self.label_r3c1.hide()
        self.label_r3c2.hide()
        self.label_r3c3.hide()
        self.label_Turn.setText("")

    def show_window(self):
        self.show()

    def print_gameboard(self):
        for x in self.gameboard:
            print(x[0] + " " + x[1] + " " + x[2] + '/n')

    #checks the gameboard rep for 3 in a row. returns 1 if p1 win, returns 2 if p2 win, returns n if no win
    def check_win(self):
        #check rows
        i = 0
        while i < 3:
            if self.gameboard[i][0] == self.gameboard[i][1] == self.gameboard[i][2]:
                return self.gameboard[i][0]
            i += 1
        #check columns
        i = 0
        while i < 3:
            if self.gameboard[0][i] == self.gameboard[1][i] == self.gameboard[2][i]:
                return self.gameboard[0][i]
            i += 1
        #check diag
        if self.gameboard[0][0] == self.gameboard[1][1] == self.gameboard[2][2]:
            return self.gameboard[0][0]
        if self.gameboard[2][0] == self.gameboard[1][1] == self.gameboard[0][2]:
            return self.gameboard[2][0]
        
        #no win
        return 'n'

    #move functions general algo
    #1. change hidden label text to player's symbol
    #2. change position is list representation
    #3. hide push button, show modified label
    #4. swap turn and turn label

    def set_turn_label(self):
        if self.p1_turn:
            self.label_Turn.setText("It's " + self.p1_name + "'s turn")
        else:
            self.label_Turn.setText("It's " + self.p2_name + "'s turn")
    
    def r1c1_move(self):
        if self.p1_turn:
            self.label_r1c1.setText(self.p1_symbol)
            self.gameboard[0][0] = '1'
        else:
            self.label_r1c1.setText(self.p2_symbol)
            self.gameboard[0][0] = '2'
        self.pushButton_r1c1.hide()
        self.label_r1c1.show()
        self.print_gameboard()
        self.p1_turn = not self.p1_turn
        self.set_turn_label()

    def r1c2_move(self):
        if self.p1_turn:
            self.label_r1c2.setText(self.p1_symbol)
            self.gameboard[0][1] = '1'
        else:
            self.label_r1c2.setText(self.p2_symbol)
            self.gameboard[0][1] = '2'
        self.pushButton_r1c2.hide()
        self.label_r1c2.show()
        self.print_gameboard()
        self.p1_turn = not self.p1_turn
        self.set_turn_label()

    def turn_driver(self):
        #set turn label
        self.set_turn_label()
        if self.p1_turn:
            #function for each possible move
            self.pushButton_r1c1.clicked.connect(self.r1c1_move)
            self.pushButton_r1c2.clicked.connect(self.r1c2_move)
        else:
            self.pushButton_r1c1.clicked.connect(self.r1c1_move)
            self.pushButton_r1c2.clicked.connect(self.r1c2_move)

        #swap turn(in rXcX_move functions)


    def game_driver(self):
        #choose who goes first
        self.p1_turn = bool(random.getrandbits(1))
        playing = True

        #big while loop
        while playing:
            #do turn, change 
            self.turn_driver()
            #check for win

            #if win, break loop and reward wins/losses
            playing = False


        

#use QTable Widget to display all profiles and profile statistics
class stat_window(QDialog):
    def __init__(self):
        #setup
        super(stat_window,self).__init__()
        loadUi('statswindow.ui',self)
        self.player_profiles = []
        #functionality
        #done button
        self.pushButton_Done.clicked.connect(self.close_window)

    #closes window
    def close_window(self):
        self.close()

    #shows window
    def show_window(self):
        self.show()

    #info pass test. function will print all info passed in to player_profiles onto a label
    #function. rework into a list later?
    def print_label(self):
        toBePrinted = ""
        for x in self.player_profiles:
            toBePrinted += x.name +" | " + x.symbol + " | " + str(x.wins) + " - " + str(x.losses) + " - " + str(x.draws) + "\n"
        self.label_TestPrint.setText(toBePrinted)

class main_window(QDialog): 
    def __init__(self):
        #setup
        super(main_window,self).__init__()
        loadUi('mainwindow.ui',self)
        #nested list: profile format -> [name, symbol, win, loss, draws]
        self.player_profiles = []
        self.stat_window = stat_window()
        self.game_window = game_window()
        
        #functionality
        #open stats button
        self.pushButton_Stats.clicked.connect(self.op_stats)
        #create profile button
        self.pushButton_CreateProfile.clicked.connect(self.create_profile)
        #play game button
        self.pushButton_Play.clicked.connect(self.play_game)

    #opens stat window and passes player_profiles into it
    def op_stats(self):
        self.stat_window.player_profiles = self.player_profiles
        self.stat_window.show_window()
        self.stat_window.print_label()

    #opens the game window and goes through a game of tictaktoe
    def play_game(self):
        #check that two users are selected
        if self.comboBox_Player1.currentText() == "":
            self.label_PlayError.setText("[ERROR] Create 2 profiles first...")
            return
        #check that two different users are selected in combo boxes 
        if self.comboBox_Player1.currentText() == self.comboBox_Player2.currentText():
            if len(self.player_profiles) == 1:
                self.label_PlayError.setText("[ERROR] Make another profile")
                return
            self.label_PlayError.setText("[ERROR] No playing with urself")
            return

        self.label_PlayError.clear()

        #users are valid. pass player names and symbols into game window
        self.game_window.p1_name = self.comboBox_Player1.currentText()
        self.game_window.p2_name = self.comboBox_Player2.currentText()
        for x in self.player_profiles:
            if x.name == self.comboBox_Player1.currentText():
                self.game_window.p1_symbol = x.symbol
            if x.name == self.comboBox_Player2.currentText():
                self.game_window.p2_symbol = x.symbol
        
        #run game
        self.game_window.game_driver()
        self.game_window.show_window()
        
        

    #clears all plainTextEdit inputs
    def clear_text_inputs(self):
        self.plainTextEdit_Name.clear()
        self.plainTextEdit_Symbol.clear()

    #either creates a profile or throws an error
    def create_profile(self):
        name_input = self.plainTextEdit_Name.toPlainText()
        symbol_input = self.plainTextEdit_Symbol.toPlainText()
        #only taking the first character for symbol
        symbol_input = symbol_input[0]
        
        #check for duplicate symbol and name. if either found, throw error
        for x in self.player_profiles:
            if x.name == name_input:
                #name matches existing profile. display error to label and exit
                self.label_ProfileError.setText("[ERROR] A profile exists with this name!")
                return
            if x.symbol == symbol_input:
                #symbol matches existing profile. display error to label and exit
                self.label_ProfileError.setText("[ERROR] A profile exists with this symbol!")
                return
        
        #name and symbol valid. append to player_profiles, clear inputs, success message
        new_profile = player_profile(name_input, symbol_input)
        self.player_profiles.append(new_profile)
        self.label_ProfileError.setText(name_input + "'s profile has been created!")
        self.clear_text_inputs()
        
        #add created profile as an option in both comboBoxes
        self.comboBox_Player1.addItem(name_input)
        self.comboBox_Player2.addItem(name_input)

#start and show app
app = QApplication(sys.argv)
widget = main_window()
widget.show()

sys.exit(app.exec_())
