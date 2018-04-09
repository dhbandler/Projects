#Daniel Bandler
#4/4/18
#HangmanGraphics.py --- makes a hangman game graphically
from ggame import *
from random import randint

def pickWord():  #Selects the word
    num = randint(1,10)
    if num == 1:
        word = "happinessx"
        return word
    elif num == 2:
        word = "mechanizedx"
        return word
    elif num == 3:
        word = "weddingx"
        return word
    elif num == 4:
        word = "airportx"
        return word
    elif num == 5:
        word = "realpolitikx"
        return word
    elif num == 6:
        word = "beelzebubx"
        return word
    elif num == 7:
        word = "fraternalx"
        return word
    elif num == 8:
        word = "schadenfreudex"
        return word
    elif num == 9:
        word = "intelligentsiax"
        return word
    else:
        word = "carthagex"
        return word
      
def charact(): #Prints lines under letters for guess
    charcount = len(word)
    z = 350
    for i in range(1,charcount+1):
        Sprite(wordunderline, (z, 450))
        z += 25
     
     
def keyPress(event):
    
    if event.key in word:  #Deals with what happens when you get it right
        text = TextAsset(event.key, fill=black,style= "bold 30pt Georgia")
        Sprite(text)
        data["correct guesses"] += 1
        
    else:   #Deals with the "What if?"'s of getting it wrong
        text = TextAsset(i, fill=black,style= "bold 30pt Georgia")
        Sprite(text)
        data["incorrect guesses"] += 1 
        if data["incorrect guesses"] == 1:
            Sprite(head, (200,140))
        elif data["incorrect guesses"] == 2:
            Sprite(body, (235,220))
        elif data["incorrect guesses"] == 3:
            Sprite(limbs, (225,295))
        elif data["incorrect guesses"] == 4:
            Sprite(limbs, (245,295)) 
        elif data["incorrect guesses"] == 5:
            Sprite(blackLine, (230, 220))
        elif data["incorrect guesses"] == 6:
            Sprite(blackLine2, (190, 220))
            Sprite((TextAsset("you died", fill=black,style= "bold 100pt Georgia")), (300, 200))
    
   

if __name__ == '__main__':
    
    data = {}  #These are for storing number of correct and incorrect guesses
    data["incorrect guesses"] = 0
    data["correct guesses"] = 0


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
    body = RectangleAsset(5,75, blackOutline, white)
    limbs = RectangleAsset(5,50, blackOutline, white)
    blackLine = LineAsset(50,50, blackOutline)
    blackLine2 = LineAsset(-50,50, blackOutline)
    wordunderline = RectangleAsset(15,5, blackOutline, black)
    

    #Sprites constants
    Sprite(wood1, (50,50))
    Sprite(wood2, (50,50))
    Sprite(wood2, (0,450))
    Sprite(rope1, (240,75))
    Sprite(rope2, (228,150))
    Sprite(ropespace, (231, 153))
    
    #Keyboard input:
    
    word = pickWord()
    
    charact()
    
    for i in str("abcdefghijklmnopqrstuvwxyz"):
        App().listenKeyEvent("keydown", i, keyPress)
        
        
    
    App().run(pickWord)
