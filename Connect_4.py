## Tkinter practice
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
    # fill lowest empty piece 
    canvas.itemconfig(board[row][col], fill=plyr)
    canvas.itemconfig(board[row][col], tags=(plyr))
    checkWin(row, col, vertical)
    if not gameOver:
        checkWin(row, col, horizontal)
    if not gameOver:
        checkWin(row, col, downRight)
    if not gameOver:
        checkWin(row, col, upRight)
    
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
    global gameOver, board, canvas, plyr, winCoords
    count = 0
    startCoords=[]
    endCoords=[]
    ## Get coords of piece to start/end line
    ## start & end (x1+x2) / 2, (y1+y2) / 2
    
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
                if count==1:
                    startPoint = canvas.coords(p)
                if count==4:
                    addLineCoords(startPoint, "start")
                    addLineCoords(canvas.coords(p),"end")
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
                if count==1:
                    startPoint = canvas.coords(p)
                if count==4:
                    addLineCoords(startPoint, "start")
                    addLineCoords(canvas.coords(p), "end")
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
                if count==1:
                    startPoint = canvas.coords(p)
                if count==4:
                    addLineCoords(startPoint, "start")
                    addLineCoords(canvas.coords(p), "end")
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
                if count==1:
                    startPoint = canvas.coords(p)
                if count==4:
                    addLineCoords(startPoint, "start")
                    addLineCoords(canvas.coords(p), "end")
                    gameOver = True
            else:
                count=0
            if col+1 <=6 and row-1 >= 0:
                col+=1
                row-=1
            else:
                break
    
    if gameOver:
        canvas.create_line(winCoords["x1"], winCoords["y1"], winCoords["x2"], winCoords["y2"], fill="#FCFCFC", width="3p", arrow=tk.BOTH)

def addLineCoords(coords, pos):
    global winCoords
    if pos == "start":
        winCoords["x1"] = (coords[0] + coords[2]) / 2
        winCoords["y1"] = (coords[1] + coords[3]) / 2
    elif pos == "end":
        winCoords["x2"] = (coords[0] + coords[2]) / 2
        winCoords["y2"] = (coords[1] + coords[3]) / 2

def pretty(event):
    print("VERY NICE!!!")

def newGame():
    global canvas, newGameButton,colors, p1,p2
    colors = ["red","black","green","blue","magenta"]
    p1 = ''
    p2 = ''
    canvas.delete("all")
    newGameButton.pack_forget()
    showColorOptions("1")

def setupBoard():
    global gameOver, canvas, gameText, board, plyr
    # Draw the board
    canvas.delete(ALL)
    board=[]
    gameText=""
    gameOver=False
    plyr = p1
    colStart = 55
    rowStart = 50
    rowPos = rowStart
    colPos = colStart
    for x in range(6):
        new_list=[]
        for y in range(7):
            spot = canvas.create_oval(colPos, rowPos, colPos+45, rowPos+45, fill="white", tags=("piece",y))
            colPos += 55
            new_list.append(spot)
        rowPos += 50
        colPos = colStart
        board.append(new_list)
    canvas.tag_bind("piece", '<Button-1>', select)
    gameText = canvas.create_text(250, rowPos + 65, fill=plyr, font='Arial 20 bold', text=plyr.upper() + "'s TURN")
    canvas.pack()

def pickColor(event):
    global p1, p2, gameText, colors
    if p1 == '':
        p1 = canvas.gettags(CURRENT)[0]
        colors.remove(p1)
        canvas.delete(colors[-1])
        canvas.delete(p1)
        showColorOptions("2")
    else:
        p2 = canvas.gettags(CURRENT)[0]
        setupBoard()

def showColorOptions(p):
    global colors, gameText, p1
    if p == "1":
        gameText = canvas.create_text(250, 300, font='Arial 20 bold', text="Player " + p + " - Choose your color")
    else:
        canvas.itemconfig(gameText, text="Player " + p + " - Choose your color")
    startX = 65
    startY = 150
    for color in colors:
        option = canvas.create_oval(startX, startY, startX+45, startY+45, fill=color, tags=color)
        canvas.tag_bind(color, '<Button-1>', pickColor)
        startX+=80
    
    
root = tk.Tk()
root.title("CONNECT 4")
root.geometry('500x550')

## Directions to check
vertical = 1
horizontal = 2
downRight = 3
upRight = 4

## Coordinates for the drawing the winning line
winCoords = {}
gameOver = False
p1 = ''
p2 = ''
plyr=p1
board = []
colors = []
canvas = Canvas(root, width=500, height=500, bg="#DCDCDC")
canvas.pack()
gameText = canvas.create_text(250, 300, font='Arial 20 bold', text="Player 1 - Choose your color")
newGameButton = Button(root, text="New Game", command=newGame, justify=CENTER)
newGame()
root.mainloop()

## To interact w objects in canvas, use tag_bind()
## tag_bind(item, event=None, callback, add=None)
## item can be a tag or id

#    canvas.addtag_withtag("red", CURRENT)
# We can get the type of object selected
#print(canvas.type(CURRENT))
# We can get the color of the piece
#print(canvas.itemcget(CURRENT, 'fill'))