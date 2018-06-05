#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import *
from random import randint

rowcols = int(input("Enter the number of rows you want.  "))
shipNum = int(input("Enter the number of subs you want.  "))

ROWS = rowcols
COLS = rowcols
CELL_SIZE = ROWS*18


def buildBoard():
    return [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
    

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()

    for i in range(rowcols):
        for j in range(rowcols):
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE, j*CELL_SIZE))
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE+CELL_SIZE*6, j*CELL_SIZE))
            
            if data["board"][i][j] == "ship":
                Sprite(shipbox,(i*CELL_SIZE,j*CELL_SIZE))
                
            elif data["board"][i][j] == "sunk":
                Sprite(sunk,(i*CELL_SIZE,j*CELL_SIZE))

            elif data["board"][i][j] == "miss":
                Sprite(miss,(i*CELL_SIZE,j*CELL_SIZE))
            
            if data["compboard"][i][j] == "miss":
                Sprite(miss,(i*CELL_SIZE+CELL_SIZE*6,j*CELL_SIZE))
            
            elif data["compboard"][i][j] == "sunk":
                Sprite(sunk,(i*CELL_SIZE+CELL_SIZE*6,j*CELL_SIZE))
                
            if data["THEIRSUNK"] == shipNum:
                Sprite((TextAsset("YOU WIN!!", fill=green,style= "bold 75pt Georgia")), (200, 50))
                
            if data["SUNK"] == shipNum:
                Sprite((TextAsset("YOU LOOOOSSSEEEE!!!!!!", fill=red,style= "bold 75pt Georgia")), (10, 50))
               

            

def mouseClick(event):

    
    if data["totalClicks"] < shipNum:
        if data["compboard"] != "ship":
            data["board"][event.x//CELL_SIZE][event.y//CELL_SIZE] = "ship"
            redrawAll()
            data["totalClicks"] += 1
        

    if data["totalClicks"] >= shipNum:
        if data["compboard"] != "sunk" and data["compboard"] != "miss":
            if data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] == "ship":
                data["totalClicks"] += 1
                data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] = "sunk"
                data["THEIRSUNK"] += 1
            else:
                data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] = "miss"
                data["totalClicks"] += 1
            computerTurn()
            redrawAll()
            



def pickComputerShips():
    i = 0
    while i < shipNum:
        rand1 = randint(0,rowcols-1)
        rand2 = randint(0,rowcols-1)
        if data["compboard"] != "ship":
            data["compboard"][rand1][rand2] = "ship"
            i += 1
    print(data["compboard"])


def computerTurn():
    cord1 = randint(0,rowcols-1)
    cord2 = randint(0,rowcols-1)
    if data["board"][cord1][cord2] == "miss" or data["board"][cord1][cord2] == "sunk": 
        computerTurn()
    else:
        if data["board"][cord1][cord2] == "ship":
            data["board"][cord1][cord2] = "sunk"
            data["SUNK"] += 1
            
        else:
            data["board"][cord1][cord2] = "miss"
            
            
    
    

if __name__== "__main__":

    data = {}
    data["board"] = buildBoard()
    data["compboard"] = buildBoard()
    data["totalClicks"] = 0
    data["SUNK"] = 0
    data["THEIRSUNK"] = 0

    
   

    blue = Color(0x3383FF,1)
    chrome = Color(0xdbe4eb,1)
    black = Color(0x000000,1)
    green = Color(0x008000,.5)
    red = Color(0xFF0000,.5)

    shipbox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),chrome)
    miss = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(5,black),green)
    sunk = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(5,black),red)


    pickComputerShips()
    
    redrawAll()
    
    App.listenMouseEvent("click", mouseClick)

    App().run()
