#You are responsible for writing a program that will allow two users to play a game of tic tac toe.
#Your program should follow the standard rules in which two players alternate turns putting their
#pieces, X or O, on a board. If a player has three pieces in a row, either vertically, horizontally,
#or diagonally, they are declared the winner. You will represent the tic tac toe board using the
#integers 1 through 9 for the 9 spaces on the board. An empty spot on the board will be
#represented by an underscore “_”. For example, if a player would like to put a piece in the
#center of the board they would enter 5 as their move.

#Initialise list of possible player moves
possible_moves = [1,2,3,4,5,6,7,8,9]
#Initialise list of player's moves on the board
player_moves = ["-"]*9

#Function to print tic-tac-toe board
def generate_board(board_squares):
    print("\n\t   Tic-Tac-Toe")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {board_squares[0]} || {board_squares[1]} || {board_squares[2]} ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {board_squares[3]} || {board_squares[4]} || {board_squares[5]} ||")
    print("\t~~~~~~~~~~~~~~~~~")
    print(f"\t|| {board_squares[6]} || {board_squares[7]} || {board_squares[8]} ||")
    print("\t~~~~~~~~~~~~~~~~~")

#Function to record player move on board
def add_move(Xs_turn, player_move):
    if Xs_turn:
        player_moves[player_move - 1] = "X"
    else:
        player_moves[player_move - 1] = "O"

#Function to check whether there's a win state
def check_win(m_h, X_turn):
    if X_turn:
        counter = "X"
    else:
        counter = "O"
    if ((m_h[0] == counter and m_h[1] == counter and m_h[2] == counter) or
     (m_h[3] == counter and m_h[4] == counter and m_h[5] == counter) or
     (m_h[6] == counter and m_h[7] == counter and m_h[8] == counter) or
     (m_h[0] == counter and m_h[3] == counter and m_h[6] == counter) or
     (m_h[1] == counter and m_h[4] == counter and m_h[7] == counter) or
     (m_h[2] == counter and m_h[5] == counter and m_h[8] == counter) or
     (m_h[0] == counter and m_h[4] == counter and m_h[8] == counter) or
     (m_h[2] == counter and m_h[4] == counter and m_h[6] == counter)):
        return True
    else:
        return False

#Initialise flag for starting player
player_X_turn = True

#Generate initial board state
generate_board(possible_moves)
generate_board(player_moves)

while True:
    #Player inputs
    if player_X_turn:
        move = int(input("X: Where would you like to place your piece(1 - 9): "))
        if move not in possible_moves:
            print("That is not a spot on the board. Try again.")
        elif player_moves[move - 1] != "-":
            print("That spot has already been chosen. Try again.")
        else:
            add_move(player_X_turn, move)
            #Update boards
            generate_board(possible_moves)
            generate_board(player_moves)
            #Check for win-state
            if check_win(player_moves, player_X_turn):
                print("\nCongrats! Player 1 wins!")
                break
            player_X_turn = False

    if player_X_turn == False:
        move = int(input("O: Where would you like to place your piece(1 - 9): "))
        if move not in possible_moves:
            print("That is not a spot on the board. Try again.")
        elif player_moves[move - 1] != "-":
            print("That spot has already been chosen. Try again.")
        else:
            add_move(player_X_turn, move)
            #Update boards
            generate_board(possible_moves)
            generate_board(player_moves)
            #Check for win-state
            if check_win(player_moves, player_X_turn):
                print("\nCongrats! Player 2 wins!")
                break
            player_X_turn = True
        
    #Check for Draw state
    if "-" not in player_moves:
        generate_board(player_moves)
        print("It's a draw.")
        break