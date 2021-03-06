#Daniel Bandler
#4/4/18
#HangmanGraphics.py --- makes a hangman game graphically
from ggame import *
from random import randint

def pickWord():  #Selects the word
    num = randint(0,1)
    
    choices = ["praetor", "purgatory", "perestroika","airport","realpolitik","beelzebub","fraternal","schadenfreude","intelligentsia","incendiary","dachshund","petroleum","electroencephalograph","antidisestablishmentarianism" "carthage"]
    return choices[num]
      
def charact(): #Prints lines under letters for guess
    charcount = len(data["word"])
    z = 350
    for i in range(1,charcount+1):
        Sprite(wordunderline, (z, 450))
        z += 25
        
      
def wordComplete():  #Finishes game if you get it correct
    for ch in data["word"]: 
                if ch not in data["lettersGuessed"]:
                    data["gameOver"] = False
                    return False
    data["gameOver"] = True
    return True
        

def keyPress(event): #Deals with what happens when you hit a key
    if data["gameOver"] == False:
        if event.key not in data["lettersGuessed"]:
            text = TextAsset(event.key, fill=black,style= "bold 30pt Georgia")
            Sprite(text, (data["guessed boxx"],data["guessed boxy"]))
            data["guessed boxx"] += 40
            if data["guessed boxx"] >= 900:
                data["guessed boxy"] += 40
                data["guessed boxx"] = 450
        
            data["lettersGuessed"] += event.key

            if wordComplete():
                 Sprite((TextAsset("YOU SAVED THE CONVICTED MURDERER!!", fill=green,style= "bold 75pt Georgia")), (75, 50))
        
            z = 350 #Sprites letters if correct
            for ch in data["word"]:
                if ch == event.key:
                    Sprite(TextAsset(event.key, fill=black,style= "bold 30pt Georgia"), (z, 410))
                z += 25
                
        
        
            if event.key not in data["word"]:   #Deals with the "What if?"'s of getting it wrong
        
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
                    Sprite((TextAsset("YOU DIED!!", fill=red,style= "bold 100pt Georgia")), (150, 100))
                    data["gameOver"] = True
        
    
   

if __name__ == '__main__':
    
    data = {}  #These are for storing number of correct and incorrect guesses
    data["incorrect guesses"] = 0
    data["guessed boxx"] = 450
    data["guessed boxy"] = 250
    data["word"] = pickWord()
    data["gameOver"] = False
    data["lettersGuessed"] = str()


    #Colors:
    black = Color(0x000000,1) #color black
    white = Color(0xFFFFFF,1) #color white
    woodbrown = Color(0x8B4513,1) #Color brown
    lightbrown = Color(0xD2691E,1)#light brown
    red = Color(0xFF0000,1) #red
    green = Color(0x008000,1) #green


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
    
 
    
    charact() #creates the correct number of underlines for the word
    
    for i in str("abcdefghijklmnopqrstuvwxyz"):  #listens for keyboard event
        App().listenKeyEvent("keydown", i, keyPress)
        
        
    
    App().run(pickWord)
