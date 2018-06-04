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

    for i in range(5):
        for j in range(5):
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE, j*CELL_SIZE))
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE+CELL_SIZE*6, j*CELL_SIZE))
            
            if data["board"][i][j] == "ship":
                Sprite(shipbox,(i*CELL_SIZE,j*CELL_SIZE))
                
            elif data["board"][i][j] == "sunk":
                Sprite(sunk,(i*CELL_SIZE,j*CELL_SIZE))

            elif data["board"][i][j] == "miss":
                Sprite(miss,(i*CELL_SIZE,j*CELL_SIZE))
            
            if data["compboard"][i][j] == "miss":
                Sprite(miss,(i*CELL_SIZE+90*6,j*CELL_SIZE))
            
            elif data["compboard"][i][j] == "sunk":
                Sprite(sunk,(i*CELL_SIZE+90*6,j*CELL_SIZE))
               

            

def mouseClick(event):

    
    if data["totalClicks"] < 3:
        data["board"][event.x//90][event.y//90] = "ship"
        redrawAll()
        

    if data["totalClicks"] >= 3:
        computerTurn()
        if data["compboard"][(event.x-(90*6))//90][event.y//90] == "ship":
            data["compboard"][(event.x-(90*6))//90][event.y//90] = "sunk"
            data["THEIRSUNK"] += 1
        else:
            data["compboard"][(event.x-(90*6))//90][event.y//90] = "miss"
        

    if data["SUNK"] >= 3:
        Sprite((TextAsset("YOU LOOOOSSSEEEE!!!!!!", fill=red,style= "bold 75pt Georgia")), (75, 50))
    data["totalClicks"] += 1        


def pickComputerShips():
    i = 0
    while i < 3:
        rand1 = randint(0,4)
        rand2 = randint(0,4)
        if data["compboard"] != "ship":
            data["compboard"][rand1][rand2] = "ship"
            i += 1
    print(data["compboard"])


def computerTurn():
    cord1 = randint(0,4)
    cord2 = randint(0,4)
    if data["board"][cord1][cord2] != "miss" or data["board"][cord1][cord2] != "sunk": 
        if data["board"] == "ship":
            data["board"][cord1][cord2] = "sunk"
            data["SUNK"] += 1
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),red),((cord1)*CELL_SIZE, (cord2)*CELL_SIZE))
        else:
            data["board"][cord1][cord2] = "miss"
            data["MISS"] += 1
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),green),((cord1)*CELL_SIZE, (cord2)*CELL_SIZE))
    if data["THEIRSUNK"] >= 3:
        Sprite((TextAsset("YOU WIN!!", fill=green,style= "bold 75pt Georgia")), (75, 50))
        
    
    

if __name__== "__main__":

    data = {}
    data["board"] = buildBoard()
    data["compboard"] = buildBoard()
    data["totalClicks"] = 0
    data["MISS"] = 0
    data["SUNK"] = 0
    data["THEIRSUNK"] = 0
    
    GuessedComp = []


    
    ComputerShips = []
    
   

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
