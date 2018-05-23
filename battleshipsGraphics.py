#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import *

ROWS = 16
COLS = 34
CELL_SIZE = 30

buildBoard = []


if __name__== "__main__":
    
    blue = Color(0x3383FF,1)
    chrome = Color(0xdbe4eb,1)
    black = Color(0x000000,1)
    
    seaBox = RectangleAsset(CELL_SIZE*COLS,CELL_SIZE*ROWS,LineStyle(1,blue),blue)
    shipBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,black),chrome)
    line = LineAsset(1*COLS,CELL_SIZE*ROWS, LineStyle(1,black))
    

    Sprite(seaBox)
    Sprite(line)
    Sprite(shipBox)
    App().run()
    