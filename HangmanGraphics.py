#Daniel Bandler
#4/4/18
#HangmanGraphics.py --- makes a hangman game graphically
from ggame import *
from random import randint

def pickWord():  #Selects the word
    num = randint(1,10)
    if num == 1:
        word = "Happiness"
    elif num == 2:
        word = "Mechanized"
    elif num == 3:
        word = "Wedding"
    elif num == 4:
        word = "Airport"
    elif num == 5:
        word = "Realpolitik"
    elif num == 6:
        word = "Beelzebub"
    elif num == 7:
        word = "Conquest"
    elif num == 8:
        word = "Schadenfreude"
    elif num == 9:
        word = "Intelligentsia"
    else:
        word = "Carthage"
        
def charact(): #Prints lines under letters for guess
    charcount = len(word)
    z = 50
    for i in range(1,charcount+1):
        Sprite(wordunderline, (z, 100))
        z += 75
        
    

if __name__ == '__main__':

    data = {}
    data["incorrect guesses"] = 0
    data["total guesses"] = 0
    


    #Colors:
    black = Color(0x000000,1) #color black
    white = Color(0xFFFFFF,1) #color white
    woodbrown = Color(0x8B4513,1) #Color brown
    lightbrown = Color(0xD2691E,1)#light brown


    blackOutline = LineStyle(5,black) #Outline
    blackOutline2 = LineStyle(1,black) #Outline

    #Shape Design:

    wood1 = RectangleAsset(50,400, blackOutline2, woodbrown)
    wood2 = RectangleAsset(200,25, blackOutline2, woodbrown)
    rope1 = RectangleAsset(5,75,blackOutline2,lightbrown)
    rope2 = EllipseAsset(15,30,blackOutline2,lightbrown)
    ropespace = EllipseAsset(12,27,blackOutline2,white)
    head = CircleAsset(40,blackOutline,white)
    body = RectangleAsset(50,75, blackOutline, white)
    limbs = RectangleAsset(25,50, blackOutline, white)
    wordunderline = RectangleAsset(15,5, blackOutline, black)

    #Sprites constants
    Sprite(wood1, (50,50))
    Sprite(wood2, (50,50))
    Sprite(wood2, (0,450))
    Sprite(rope1, (240,75))
    Sprite(rope2, (228,150))
    Sprite(ropespace, (231, 153))

    for i in range():
        

    App().run(pickWord)
