Python Practice Project:
Tic Tak Toe

New goal is to create Tic Tak Toe with the same functionality as the text-based GUI using PyQt5


Text-Based GUI:
Focus: objects and classes
Make a match history?
pseudo:

player class
    name, wins, symbol, total games
    functions:
        __init__:
            takes in name and character. wins = 0
        print_player():
            print player, their character, and their number of wins to games played
        won():
            total games ++
            wins ++
        lost():
            total games ++


board class
    2d list containing the state of the board. unplayed spaces represented by - . players pick their own characters to represent where they play
    board 3 by 3 
    functions:
        __init__:
            board created, all values "-"
        print_board():
            prints board to terminal
            doesnt return
        check_win():
            returns true if win condition is met(three in a row)
            ALGO: 
            -check rows for 3 matching char not -
            -check columns for 3 matching char not -
            -check two diagonals for matching char not -

            if found, return true
            else return false

        move(player, row, column)

game class
    board, 2 players
    each individual game is played within a game object. game functionality must exist within game class
    __init__:
        creates board object for game
    
    game_driver
        while no winner:
            print board
            p1 moves
            p2 moves
        
        when someone wins
        call .win() and .lost() for respective players
        
        exit driver
    

        
        