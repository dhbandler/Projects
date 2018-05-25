#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import *
from random import randint

ROWS = 5
COLS = 5
CELL_SIZE = 100

def buildBoard():
    board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
    return board 
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    
    for i in range(5):
        for j in range(5):
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE, j*CELL_SIZE))



def mouseClick(event):
    totalClicks == 1
    if totalClicks < 3:
        Sprite(shipbox, (mouseClick.x,mouseClick.y))
    
def pickComputerShips():
    i = 0
    while i <= 3:
        rand1 = randint(1,5)
        rand2 = randint(1,5)
        Sprite(shipbox,(board[rand1-1][rand2-1]))
        i += 1
    

def computerTurn():

    


if __name__== "__main__":

    totalClicks = 0

    blue = Color(0x3383FF,1)
    chrome = Color(0xdbe4eb,1)
    black = Color(0x000000,1)


    shipBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),chrome)


    redrawAll()
    
    pickComputerShips()

    #App.listenMouseEvent("click", mouseClick)

    App().run()
