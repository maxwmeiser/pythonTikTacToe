import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

# class game_window(QDialog):
#     def __init__(self, p1, p2):
#         #setup
#         super(game_window,self).__init__()
#         loadUi('gamewindow.ui',self)
#         #initialize gameboard representation
#         gameboard = [['-','-','-'],['-','-','-'],['-','-','-']]
        

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
            toBePrinted += x[0] +" | " + x[1] + " | " + str(x[2]) + " - " + str(x[3]) + " - " + str(x[4]) + "\n"
        self.label_TestPrint.setText(toBePrinted)



class main_window(QDialog): 
    def __init__(self):
        #setup
        super(main_window,self).__init__()
        loadUi('mainwindow.ui',self)
        #nested list: profile format -> [name, symbol, win, loss, draws]
        self.player_profiles = []
        self.stat_window = stat_window()
        #self.game_window = game_window()
        
        #functionality
        #open stats button
        self.pushButton_Stats.clicked.connect(self.op_stats)
        #create profile button
        self.pushButton_CreateProfile.clicked.connect(self.create_profile)

    #opens stat window and passes player_profiles into it
    def op_stats(self):
        self.stat_window.player_profiles = self.player_profiles
        self.stat_window.show_window()
        self.stat_window.print_label()


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
            if x[0] == name_input:
                #name matches existing profile. display error to label and exit
                self.label_ProfileError.setText("[ERROR] A profile exists with this name!")
                return
            if x[1] == symbol_input:
                #symbol matches existing profile. display error to label and exit
                self.label_ProfileError.setText("[ERROR] A profile exists with this symbol!")
                return
        
        #name and symbol valid. append to player_profiles, clear inputs, success message
        new_profile = [name_input, symbol_input, 0, 0, 0]
        self.player_profiles.append(new_profile)
        self.label_ProfileError.setText(name_input + "'s profile has been created!")
        self.clear_text_inputs()

#start and show app
app = QApplication(sys.argv)
widget = main_window()
widget.show()

sys.exit(app.exec_())
