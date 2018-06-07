#Daniel Bandler
#5/23/18
#battleshipsGame.py

from ggame import * #imports everything from ggame
from random import randint #imports the tools for generating a random integer

rowcols = int(input("Enter the number of rows and columns you want. (max of 5 please)  ")) #asks for number of rows and columns
shipNum = int(input("Enter the number of subs you want.  ")) #asks for number of ships


ROWS = rowcols #section stores data for rows, cols cell size, etc
COLS = rowcols
CELL_SIZE = 200/ROWS+45 #determines cell size


def buildBoard(): #makes the matrix

#  Morpheus: "Unfortunately, no one can be told what the Matrix is. You have to see it for yourself:"

    return [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']] 
def redrawAll(): #handles all of the graphics

    for item in App().spritelist[:]: #clears graphics
        item.destroy()
    Sprite((TextAsset("BATTLESHIPS", fill=red,style= "bold 75pt Georgia")), (150, 410))
    for i in range(rowcols): #goes through everything cell by cell
        for j in range(rowcols):
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE, j*CELL_SIZE)) #makes the ocean cells
            Sprite(RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),blue),(i*CELL_SIZE+CELL_SIZE*(rowcols+1), j*CELL_SIZE))
            
            if data["board"][i][j] == "ship": #sprites our ships
                Sprite(shipbox,(i*CELL_SIZE,j*CELL_SIZE))
                
            elif data["board"][i][j] == "sunk": #sinks our ships
                Sprite(sunk,(i*CELL_SIZE,j*CELL_SIZE))

            elif data["board"][i][j] == "miss": #sprites computer misses
                Sprite(miss,(i*CELL_SIZE,j*CELL_SIZE))
            
            if data["compboard"][i][j] == "miss": #sprites our misses
                Sprite(miss,(i*CELL_SIZE+CELL_SIZE*(rowcols+1),j*CELL_SIZE))
            
            elif data["compboard"][i][j] == "sunk": #sinks comp ships
                Sprite(sunk,(i*CELL_SIZE+CELL_SIZE*(rowcols+1),j*CELL_SIZE))
                
            if data["THEIRSUNK"] == shipNum: #ends the game with victory
                Sprite((TextAsset("YOU WIN!!", fill=green,style= "bold 75pt Georgia")), (220, 100))
                data["gameOver"] = True #ends game

                
            if data["SUNK"] == shipNum: #ends the game with loss
                Sprite((TextAsset("YOU LOSE!!!!!!", fill=red,style= "bold 75pt Georgia")), (220, 100))
                data["gameOver"] = True #ends game


               

            

def mouseClick(event): #determines what happens when you click

    if data["gameOver"] == False:
        if data["totalClicks"] < shipNum: #deals with determining where our ships are
            if (event.x//CELL_SIZE) <= (CELL_SIZE*rowcols) and event.y//CELL_SIZE <= CELL_SIZE*rowcols:
                if data["board"][event.x//CELL_SIZE][event.y//CELL_SIZE] != "ship": #prevents placing multiple ships in a square
                    data["board"][event.x//CELL_SIZE][event.y//CELL_SIZE] = "ship" #sets a ship where we clicked
                    redrawAll()
                    data["totalClicks"] += 1
        

        if data["totalClicks"] >= shipNum: #this part looks at our guesses of where their ships are
            if data["compboard"] != "sunk" and data["compboard"] != "miss":#checks that we haven't guessed there before
                if (event.x-(CELL_SIZE*(rowcols+1))//CELL_SIZE) >= CELL_SIZE*(rowcols+1) and (event.x-(CELL_SIZE*(rowcols+1))//CELL_SIZE) <= CELL_SIZE*((2*rowcols)+1): #makes sure your guess is in the right spot
                    if data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] == "ship": #deals with what happens if it is a hit
                        data["totalClicks"] += 1
                        data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] = "sunk" #sinks ship
                        data["THEIRSUNK"] += 1 #adds to theirsunk count
                    else: #deals with what happens if it is a miss
                        data["compboard"][(event.x-(CELL_SIZE*(rowcols+1)))//CELL_SIZE][event.y//CELL_SIZE] = "miss" #goes and sprites miss
                        data["totalClicks"] += 1
                    redrawAll()
                    computerTurn()
        return False    



def pickComputerShips(): #sprites computer ships
    i = 0
    while i < shipNum: #makes sure right number of ships are created
        rand1 = randint(0,rowcols-1) #randomly places them
        rand2 = randint(0,rowcols-1)
        if data["compboard"][rand1][rand2] != "ship": #makes sure it hasn't been guesed before
            data["compboard"][rand1][rand2] = "ship" #sets the ship there
            i += 1
    #print(data["compboard"]) #cheat code for scrubs


def computerTurn(): #guesses where our ships are.
    if data["gameOver"] == False:
        cord1 = randint(0,rowcols-1) #random guesses
        cord2 = randint(0,rowcols-1)
    
        if data["totalClicks"] > shipNum:
            if data["board"][cord1][cord2] == "miss" or data["board"][cord1][cord2] == "sunk": #if it has been guessed before, it generates new numbers
                computerTurn()
            else:    
                if data["board"][cord1][cord2] == "ship": #verifies if there is a ship there
                    data["board"][cord1][cord2] = "sunk" #sets the ship as sunk
                    data["SUNK"] += 1 #adds to sunk count
            
                else:
                    data["board"][cord1][cord2] = "miss" #lets the computer know that it has less a less effective intelligence agency than Lesotho, and can't find targets
        redrawAll()        
            
        return False
    

if __name__== "__main__":
    #creates everything I will use
    data = {}
    data["board"] = buildBoard()
    data["compboard"] = buildBoard() #this board represents the computer's board
    data["totalClicks"] = 0 #counts total mouse clicks
    data["SUNK"] = 0 #counts how many ships we have lost
    data["THEIRSUNK"] = 0 #counts how many ships they have lost
    data["gameOver"] = False #sees if game is over

    
   

    blue = Color(0x3383FF,1) #creates the colors for great fleet
    chrome = Color(0xdbe4eb,1)
    black = Color(0x000000,1)
    green = Color(0x008000,.5)
    red = Color(0xFF0000,.5)

    shipbox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(3,black),chrome) #creates a chrome box which our graphic designers claim looks like a ship, however I don't see it
    miss = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(5,black),green) #creates a green box which represents a miss because misses obviously turn the ocean green
    sunk = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(5,black),red) #creates a red box to signify the fire of a sinking ship


    
    pickComputerShips() #picks the computer ships
    
    redrawAll() #runs redrawAll()
    
    App.listenMouseEvent("click", mouseClick) #listens for clicks

    App().run() #runs ggame
