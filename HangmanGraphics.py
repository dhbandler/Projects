#Daniel Bandler
#4/4/18
#HangmanGraphics.py --- makes a hangman game graphically
from ggame import *
from random import randint


#Colors:
black = Color(0x000000,1) #color black
white = Color(0xFFFFFF,1) #color white
woodbrown = Color(0x8B4513,1) #Color brown
lightbrown = Color(0xD2691E,1)#light brown


blackOutline = LineStyle(5,black) #Outline
blackOutline2 = LineStyle(1,black) #Outline

#Shape Design:

head = CircleAsset(100, blackOutline, white)
wood1 = RectangleAsset(50,400, blackOutline2, woodbrown)
wood2 = RectangleAsset(200,25, blackOutline2, woodbrown)
rope1 = RectangleAsset(5,75,blackOutline2,lightbrown)
rope2 = EllipseAsset(40,25,blackOutline2,lightbrown)

#Sprites constants
Sprite(wood1, (50,50))
Sprite(wood2, (50,50))
Sprite(wood2, (0,450))
Sprite(rope1, (240,75))


App().run()