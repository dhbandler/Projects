#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import *
from random import randint

ROWS = 5
COLS = 5
CELL_SIZE = 90

def buildBoard():
    return [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
    

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    #for i in data["board"]:
        #if data["board"] == ship:
            #Sprite(shipbox,(
    for i in range(5):
        for j in range(5):
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE, j*CELL_SIZE))
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE+CELL_SIZE*6, j*CELL_SIZE))

            

def mouseClick(event):
    print(event.x//90,event.y//90)
    totalClicks += 1
    
    if totalClicks < 3:
        data["board"][event.x//90][event.y//90] = "ship"
        redrawAll()
    elif totalClicks >= 3:
        

    if SINK >= 3:
        Sprite((TextAsset("YOU LOOOOSSSEEEE!!!!!!", fill=red,style= "bold 75pt Georgia")), (75, 50))
        

def pickComputerShips():
    i = 0
    while i <= 3:
        rand1 = randint(0,4)
        rand2 = randint(0,4)
        ComputerShips.append(data["board"][rand1][rand2])
        i += 1


def computerTurn():
    cord1 = randint(0,4)
    cord2 = randint(0,4)
    if cord1 and cord2 not in GuessedComp: #This is not working right now, but is supposed to check if the coords have been guessed before
        GuessedComp.append(cord1,cord2)

    
        boardLetter = data["board"][cord1][cord2] 
        if boardLetter in myShips:
            myShips.remove(boardLetter)
            SINK += 1
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),red),((cord1+1)*CELL_SIZE, (cord2+1)*CELL_SIZE))
        else:
            MISS += 1
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),green),((cord1+1)*CELL_SIZE, (cord2+1)*CELL_SIZE))
        if THEIRSINK >= 3:
            Sprite((TextAsset("YOU WIN!!", fill=green,style= "bold 75pt Georgia")), (75, 50))
        
    
    


if __name__== "__main__":

    totalClicks = 0
    MISS = 0
    SINK = 0
    
    
    GuessedComp = []

    totalclicks = 0
    
    ComputerShips = []
    
    data = {}
    
    THEIRHIT = 0
    THEIRMISS = 0
    THEIRSINK = 0

    blue = Color(0x3383FF,1)
    chrome = Color(0xdbe4eb,1)
    black = Color(0x000000,1)
    green = Color(0x008000,1)
    red = Color(0xFF0000,1)

    shipbox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),chrome)

    data["board"] = buildBoard()
    data["compboard"] = buildBoard()
    redrawAll()
    
    pickComputerShips()

    App.listenMouseEvent("click", mouseClick)

    App().run()
