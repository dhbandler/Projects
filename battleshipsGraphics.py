#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import *

ROWS = 5
COLS = 5
CELL_SIZE = 50

def buildBoard():
    board = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
    return board 
    
def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    Sprite(seabox)
    
    
    for i in range(5):
        for j in range(5):
            Sprite(LineAsset(i*CELL_SIZE,CELL_SIZE*ROWS, LineStyle(1,black)),(i*COLS, 0))
            Sprite(LineAsset(COLS*CELL_SIZE,i*CELL_SIZE, LineStyle(1,black)), (0, i*ROWS)) 
    """
    for i in range(0,5):
        Sprite(LineAsset(i*CELL_SIZE,CELL_SIZE*ROWS, LineStyle(1,black)),(i*COLS, 0))
        Sprite(LineAsset(COLS*CELL_SIZE,i*CELL_SIZE, LineStyle(1,black)), (0, i*ROWS))
    """

def mouseClick(event):
    totalClicks == 1
    if totalClicks < 3:
        Sprite(shipbox, (mouseClick.x,mouseClick.y))
    
def pickComputerShips():

#def computerTurn():

    


    if __name__== "__main__":
    
        totalClicks = 0
    
        blue = Color(0x3383FF,1)
        chrome = Color(0xdbe4eb,1)
        black = Color(0x000000,1)
    
        seaBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,blue),blue)
        shipBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),chrome)

    
        redrawAll()
    
        #App.listenMouseEvent("click", mouseClick)
    
        App().run()
    