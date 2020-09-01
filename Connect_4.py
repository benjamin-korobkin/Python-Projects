## Tkinter practice
## TODO: Draw a line through the winning pieces
import tkinter as tk
from tkinter import *

def select(event):
    global canvas, board, plyr, p1, p2, gameText, newGameButton
    row = 0
    col = -1
    nums = ['0','1','2','3','4','5','6']
    tags = canvas.gettags(CURRENT)
    for s in tags:
        if s in nums:
           col = int(s)
    while row < 5:
        piece = board[row+1][col]
        cur_tags = canvas.gettags(piece)
        if p1 not in cur_tags and p2 not in cur_tags:
            row+=1
        else:
            break
    # fill lowest piece red
    canvas.itemconfig(board[row][col], fill=plyr)
    canvas.itemconfig(board[row][col], tags=(plyr)) # may need col too
    
    checkWin(row, col, vertical)
    checkWin(row, col, horizontal)
    checkWin(row, col, downRight)
    checkWin(row, col, upRight)
    
    ## TODO: Draw games
    draw = True
    for piece in board[0]:
        colors=canvas.gettags(piece)
        if p1 not in colors and p2 not in colors:
            draw = False
            break

    if gameOver:
        newText = plyr.upper() + " WINS!!!"
        canvas.tag_bind("piece", '<Button-1>', pretty)
        newGameButton.pack()
    elif draw:
        newText = "DRAW"
        canvas.tag_bind("piece", '<Button-1>', pretty)
        newGameButton.pack()
    else:
        if plyr == p1:
            plyr = p2
        else:
            plyr = p1
        newText = plyr.upper() + "'s TURN"

    canvas.itemconfig(gameText, fill=plyr, text=newText)
        
def checkWin(row, col, dir):
    global gameOver, board, canvas, plyr
    count = 0
    ## Check vertically
    if dir == vertical:
        for i in range(3):
            if row < 5:
                row+=1
            else:
                break
        for j in range(6):
            p = board[row][col]
            if plyr in canvas.gettags(p):
                count+=1
                if count == 4:
                    gameOver = True
            else:
                count=0
            if row-1 >= 0:
                row-=1
            else:
                break
    
    ## Horizontal
    elif dir == horizontal:
        for i in range(3):
            if col < 6:
                col+=1
            else:
                break
        for j in range(7):
            p = board[row][col]
            if plyr in canvas.gettags(p):
                count+=1
                if count==4:
                    gameOver = True
            else:
                count=0
            if col-1 >= 0:
                col-=1
            else:
                break
    
    ## downRight
    elif dir == downRight:
        for i in range(3):
            if col < 6 and row < 5:
                col+=1
                row+=1
            else:
                break
        for k in range(6):
            p = board[row][col]
            if plyr in canvas.gettags(p):
                count+=1
                if count==4:
                    gameOver = True
            else:
                count=0
            if col-1 >= 0 and row-1 >= 0:
                col-=1
                row-=1
            else:
                break
    # upRight
    elif dir == upRight:
        for i in range(3):
            if col > 0 and row < 5:
                col-=1
                row+=1
            else:
                break
        for j in range(6):
            p = board[row][col]
            if plyr in canvas.gettags(p):
                count+=1
                if count==4:
                    gameOver = True
            else:
                count=0
            if col+1 <=6 and row-1 >= 0:
                col+=1
                row-=1
            else:
                break
    
def pretty(event):
    print("VERY NICE!!!")

def newGame():
    global board, gameText, canvas, plyr, newGameButton, gameOver
    newGameButton.pack_forget()
    canvas.delete("all")
    board=[]
    gameText=""
    gameOver=False
    plyr = p1
    colStart = 55
    rowStart = 50
    rowPos = rowStart
    colPos = colStart
    # Populate the board with the pieces
    for x in range(6):
        new_list=[]
        for y in range(7):
            spot = canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
            colPos += 55
            new_list.append(spot)
        rowPos += 50
        colPos = colStart ## reset back to left side
        board.append(new_list)

    canvas.tag_bind("piece", '<Button-1>', select)
    gameText = canvas.create_text(250, rowPos + 65, fill=plyr, font='Arial 20 bold', text=plyr.upper() + "'s TURN")
    #canvas.create_text(x, y, fill='', font='', text='')
    canvas.pack()
    
#canvas.itemconfig(board[0][2], fill="red")
## pieces are configured as: board[row][column]

#for column in board:
#    for piece in column:
#        canvas.itemconfig(piece, fill="red")

root = tk.Tk()

## Directions to check
vertical = 1
horizontal = 2
downRight = 3
upRight = 4

## TODO Allow customized colors
p1 = 'red'
p2 = 'black'

gameOver = False
## Rename window title
root.title("CONNECT 4")
## Set window size

root.geometry('500x550')
board = []
canvas = Canvas(root, width=500, height=500, bg="white")
canvas.pack()
gameText=""
newGameButton = Button(root, text="New Game", command=newGame, justify=CENTER)
newGameButton.pack()
## Essential
root.mainloop()

## To interact w objects in canvas, use tag_bind()
## tag_bind(item, event=None, callback, add=None)
## item can be a tag or id

#if 'red' in tags or 'black' in tags:
    #    print("FILLED")
    #else:
    #    print("EMPTY")
    #    canvas.itemconfig(CURRENT, fill="red")
    #    canvas.addtag_withtag("red", CURRENT)
    # We can get the type of object selected
    #print(canvas.type(CURRENT))
    # We can get the color of the piece
    #print(canvas.itemcget(CURRENT, 'fill'))

    #if plyr==1:
        #canvas.itemconfig("current", fill="red")
        #plyr=2
    #else:
        #canvas.itemconfig("current", fill="black")
        #plyr=1