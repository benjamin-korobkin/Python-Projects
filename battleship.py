# This allows us to produce random numbers
from random import randint

# Initialize an empty board
board = []

# Fill the board with O's
for x in range(5):
  board.append(["O"] * 5)

# Print the board nicely
def print_board(board):
  for row in board:
    print " ".join(row)

# Produce a random spot for the ship
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
# Used for debugging. Remove to hide location of ship
#print ship_row
#print ship_col

# You get 4 turns to guess
for turn in range(4):
  print "turn: " + str(turn)
  print_board(board)
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sunk my battleship!"
    break
  elif (guess_row not in range(5)) or (guess_col not   in range(5)):
    print "Oops, that's not even in the ocean."
  elif(board[guess_row][guess_col] == "X"):
    print "You guessed that one already."
  else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X" 
  if turn == 3:
    print "Game Over"
turn += 1