from random import randrange

board = []

for i in range(5):
    board.append(['O'] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_row(board):
    return randrange(len(board))
def random_col(board):
    return randrange(len(board[0]))
ship_row = random_row(board)
ship_col = random_col(board)
# Used for debugging. Remove to hide location of ship
#print (ship_row + 1)
#print (ship_col + 1)

# You get 5 turns to guess
turn = 5
while turn > 0:
    print( "turns left: " + str(turn))
    print_board(board)
    guess_row = int(input("Guess Row (1-5): ")) - 1
    guess_col = int(input("Guess Col (1-5): ")) - 1

    if guess_row == ship_row and guess_col == ship_col:
        print( "Congratulations! You sunk my battleship!")
        break
    elif (guess_row not in range(len(board))) or (guess_col not in range(len(board[0]))):
        print ("Oops, that's not even in the ocean.")
    elif board[guess_row][guess_col] == "X":
        print ("You guessed that one already.")
    else:
        print ("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        turn -= 1
    if turn < 0:
        print ("Game Over")
