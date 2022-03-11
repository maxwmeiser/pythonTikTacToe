import profile
from symtable import Symbol
from venv import create
from board import board
from player import player
from game import game
from game import check_in
import random

#prints menu
def print_menu():
    print("\n------Menu------")
    print("1. Play a game")
    print("2. Add new player profile")
    print("3. View player profiles")
    print("4. Game Tutorial")
    print("5. Quit")

#this function creates player profiles
def create_player(player_profile_count, player_profiles):
    profile_name = input("\nCreating player profile...\nInput the name of your profile\n#> ")
    profile_symbol = input("Hey " + profile_name + ". What symbol would you like to use?\n#> ")
    #take first character entered
    profile_symbol = profile_symbol[0]

    #check if other player profiles 
    i = 0
    while player_profile_count > i:
        if profile_symbol == player_profiles[i].symbol:
            print("That symbol is already taken! Randomly picking your symbol...")
            profile_symbol = chr(random.randrange(48,93))
            print(profile_name + "'s symbol is " + profile_symbol)
        i += 1
    
    #if invalid symbol
    if profile_symbol == "" or profile_symbol == "-":
        print("Invalid symbol! Randomly picking your symbol...")
        profile_symbol = chr(random.randrange(48,93))
        print(profile_name + "'s symbol is " + profile_symbol)
    #add to profiles list
    new_player = player(profile_name,profile_symbol)
    player_profiles.append(new_player)
    print("Profile successfully added!")
    return 1

def list_players(profile_count,profiles, winrate_flag):
    i = 0
    print("\n----Player Profiles----")
    while profile_count > i:
        print(str(i) + ") Name: " + profiles[i].name + " |Symbol: " + profiles[i].symbol, end="")
        if winrate_flag:
            print(" |Winrate: " + profiles[i].winrate())
        else:
            print("\n")   
        i += 1 

PLAY = True
player_profile_count = 0
player_profiles = []

print("----Tic Tak Toe----")

   

#TODO:
#create new_player function (make dictionary key all lowercase)
#call function twice before PLAY to initiate game
#complete the rest of the menu
#when selecting players for a game present a list of player profiles

# while PLAY:
#     print_menu()
#     menu_choice = input("#>")
#     while not check_in(menu_choice,0,5):
#         menu_choice = input("Invalid input. Try again\n#>")
#     match(int(menu_choice)):
#         case 1:
#             #Play a game
            
#         case _:
#             #default
#             print("Invalid Input. Please redo")
