board = ["-","-","-",
        "-","-","-",  
        "-","-","-"]

#if game still going
game_still_going = True
#Who won? Or tie?
winner = None
#Whos turn is it
current_player = "X"

#display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

#game tic tac toe
def play_game():

    display_board()
    #game is still going
    while game_still_going:

        handle_turn(current_player)
        #check if game ended
        check_if_game_over()
        #flip to other player
        flip_player()

     #game has ended winner X or O
    if winner == "X" or winner == "O":
        print(winner + " has won.")
    elif winner == None:
        print("Tie.") 


def handle_turn(player):
    print(player + " it's your turn.")
    position = input("Choose a position from 1-9: ")
    
    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) -1
    
        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. The field is already occupied. Please choose another one. ")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()
    
def check_for_winner():
  #set up global variables
    global winner
  #check rows columns diagonals 
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()
    #Get winner or no winner
    if row_winner:
      winner = row_winner
    elif column_winner:
      winner = column_winner
    elif diagonal_winner:
      winner = diagonal_winner
    else:
      winner = None     
    return

def check_rows():
  #set up global variables
    global game_still_going
  #check row values and not epmty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[6] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
   #Return the winner (X or O)     
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]   
    return

def check_columns():
      #set up global variables
    global game_still_going
  #check column values and not epmty
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_still_going = False
   #Return the winner (X or O)     
    if column_1:
        return board[0]
    elif column_2:
        return board[2]
    elif column_3:
        return board[3]   
    return

def check_diagonals():
        #set up global variables
    global game_still_going
  #check diagonal values and not epmty
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"
    if diagonal_1 or diagonal_2:
        game_still_going = False
   #Return the winner (X or O)     
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]   
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return
    
def flip_player():
  #set up global variables
    global current_player
    #change player between O and X
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"  
    return
play_game()
