from board import board
from player import player
from game import game
from game import check_in
import random

#TODO:
#DRAW logic
#rework winrates into Wins-Losses-Draws

#prints menu
def print_menu():
    print("\n------Menu------")
    print("1. Play a game")
    print("2. Add new player profile")
    print("3. View player profiles")
    print("4. Stat Info")
    print("4. Quit")

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
        print(str(i) + ") Name: " + profiles[i].name + " | Symbol: " + profiles[i].symbol, end="")
        if winrate_flag:
            print(" | Record: " + profiles[i].winrate())
        else:
            print("\n")   
        i += 1 

PLAY = True
player_profile_count = 0
player_profiles = []

print("----Tic Tak Toe----")

#creating 2 profiles
print("Please create two player profiles to continue...")
player_profile_count += create_player(player_profile_count,player_profiles)
player_profile_count += create_player(player_profile_count,player_profiles)

#start menu loop
while PLAY:
    print_menu()
    menu_choice = input("#> ")
    while not check_in(menu_choice,0,6):
        menu_choice = input("Invalid input. Try again\n#> ")
    match(int(menu_choice)):
        case 1:
            #Play a game
            list_players(player_profile_count,player_profiles,False)
            print("Please select two players for the game\n")
            firstplayer = input("Player 1 \n#> ")
            while not check_in(firstplayer, -1, player_profile_count):
                print("Invalid player! Please input a number between 0 and " + str(player_profile_count - 1))
                firstplayer = input("#> ")
            secondplayer = input("Player 2 \n#> ")
            while not check_in(secondplayer, -1, player_profile_count) or secondplayer == firstplayer:
                print("Invalid player! Please input a unique number between 0 and " + str(player_profile_count - 1))
                secondplayer = input("#> ")
            game_instance = game(player_profiles[int(firstplayer)],player_profiles[int(secondplayer)])
            game_instance.game_driver()
        case 2:
            #Add new player profile
            player_profile_count += create_player(player_profile_count, player_profiles)
        case 3:
            #View profiles
            list_players(player_profile_count, player_profiles, True)
        case 4:
            print("Wins-Losses-Draws")
        case 5:
            #quitting
            PLAY = False
            print("Thanks for playing! Here are the stats:")
            list_players(player_profile_count, player_profiles, True)
            print("Goodbye!")
        case _:
            #default
            print("Invalid Input.")   
