# Assignment: Final project Treasure Hunt 
# Description: Treasure Hunt game 
# Name: Adam Izzet
# Date: feb 2, 2021
# Course Code: ICS2O1-03B 


#Import & initialize the pygame module
import pygame

import random 

# Make Enemy class
class Enemy (pygame.sprite.Sprite):
   def __init__(self, xCoord, yCoord, xDirection, yDirection, speed):

# Make surface for enemy         
       pygame.sprite.Sprite.__init__(self)     
       self.image = pygame.Surface((30, 30))
       self.image.blit(badG, (0, 0))
       self.image.set_colorkey((255, 255, 255))

# Make rect for enemy        
       self.rect = self.image.get_rect()
       self.rect.centery = yCoord
       self.rect.centerx = xCoord
# update x and y direction and speed
       self.xdir = xDirection
       self.ydir = yDirection

       self.speed = speed

   def update(self):
# Move the enemy 
      self.rect.centerx = self.rect.centerx + self.xdir * self.speed
      self.rect.centery = self.rect.centery + self.ydir * self.speed

# bounce enemy off the wall
      if self.rect.centerx <= 15 or self.rect.centerx >= screen.get_width() - 15:
         self.xdir = -self.xdir

      if self.rect.centery <= 15 or self.rect.centery >= screen.get_height() - 115:
         self.ydir = -self.ydir
 
      
# Make Treasure class 
class Treasure (pygame.sprite.Sprite):
    def __init__(self, xCoord, yCoord):
# Make surface for treasure 
       pygame.sprite.Sprite.__init__(self)
       self.image = pygame.Surface((30, 30))
       self.image.blit(treasurePic, (0, 0))
       self.image.set_colorkey((255, 255, 255))

# Make rect for treasure 
       self.rect = self.image.get_rect()
       self.rect.centery = yCoord
       self.rect.centerx = xCoord
 
 
# Make the player class 
class Player(pygame.sprite.Sprite):
   
   
   def __init__(self,char, x, y, lives):
      pygame.sprite.Sprite.__init__(self)
      
      
# Make surface for main character       
      self.image = pygame.Surface((30, 30))
      self.image.blit(char, (0, 0))
      self.image.set_colorkey((255, 255, 255))
      
# Make rect for main character surface      
      self.rect = self.image.get_rect()
      self.rect.centery = y
      self.rect.centerx = x
      
   def update(self):
# update position of the main character  
      self.rect.centerx = x 
      self.rect.centery = y
      
       
#pygame.locals contains constants like MOUSEMOTION and MOUSEBUTTONUP and QUIT for events. 
#It's easier to type MOUSEBUTTONUP instead of pygame.locals.MOUSEBUTTONUP
from pygame.locals import *  

#This will allow us to name the colours to use rather than give a name eg (255,0,0)
from pygame.color import THECOLORS
 
pygame.init()  

#Just like python, we will use os and time
import os, time

#this code is necessary for python to work on tdsb computers
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'

#Set-up the main screen display window and caption in the 
size = (800, 800) 
screen = pygame.display.set_mode(size)

#Puts a caption in the bar at the top of the window
pygame.display.set_caption("Hunt the Treasure") 


#Update and refresh the display to end this frame
pygame.display.flip() #<-- refresh the displayy


#Some game loop settings
clock = pygame.time.Clock() #<-- used to control the frame rate
 
 
treasurePic = pygame.image.load("Coin.png").convert()
treasureGrp = pygame.sprite.Group()  
masterGrp = pygame.sprite.Group()        
        
# create 30 pieces of treasure
for i in range(1,31):

# Make random spawn cords for the 30 pieces of treasure on screen   
    xcoord = random.randrange(0, 800)
    ycoord = random.randrange(0, 685)
         
# Spawn treasure at random cords
# Add treasure to treasure grp and add treasure to all item grp         
    newTreasure = Treasure(xcoord,ycoord)
    treasureGrp.add(newTreasure)
    masterGrp.add(newTreasure)     

# import bad guy picture and make bad guy grp                   
badG = pygame.image.load("ee30.png").convert()
badGuysGrp = pygame.sprite.Group()
    
    
# create 10 bad guys
for i in range(1,11):

# Make random spawn cords and directions and speeds for the 10 bad guy on screen  
   xCoord = random.randrange(15, screen.get_width() - 15)
   yCoord = random.randrange(15, screen.get_height() - 115)
   xdir = random.choice([-1, 1])
   ydir = random.choice([-1, 1])
   speed2 = random.randrange(4,10)
   
# Spawn bad guys at random cords and directions and speed
# add bad guy to bad guy grp and add bad guy to all item grp 
   newEnemy = Enemy(xCoord, yCoord, xdir, ydir,speed2)
   badGuysGrp.add(newEnemy)
   masterGrp.add(newEnemy)


# add mainChar picture
mainChar = pygame.image.load("TT30.png").convert()
x = 400 
y = 685  

# Make good guy with 40 lifes and add to good guy grp and all item grp      
goodG = Player(mainChar, x, y, 40) 
goodGuysGrp = pygame.sprite.Group()
goodGuysGrp.add(goodG) 
masterGrp.add(goodG)

# Set game score and player lives  
score = 0
lives = 40

# Make winner and loser screen msg 
customFont = pygame.font.SysFont("Times New Roman", 40)
lose = customFont.render("GAME OVER - GG", True, (255, 255, 255)).convert_alpha()
win = customFont.render("WINNER", True, (255, 255, 255)).convert_alpha()



# variable used to determine if the game should continue
keepGoing = True
#The game loop
while keepGoing:
    clock.tick(30) #<-- Set a constant frame rate, argument is frames per second

# Draw good guy, bad guy and treasure
    screen.fill((255, 255, 255))
    treasureGrp.draw(screen)
    badGuysGrp.draw(screen)
    badGuysGrp.update()
    goodGuysGrp.draw(screen)
    goodGuysGrp.update()
    screen.blit(goodG.image, goodG.rect)
    
    keys = pygame.key.get_pressed()

    
# draw red bar and game score and player health at bottem of the screen     
    pygame.draw.rect(screen, ('red'), (0, 700, 800, 100))
    
    gameScore = customFont.render("score:" + str(score), True, (10, 100, 241)).convert_alpha()
    screen.blit(gameScore , (150, 725))
 
    health = customFont.render("lives:" + str(lives), True, (10, 100, 241)).convert_alpha()
    screen.blit(health , (500, 725))
    
# increase the score by one when the player collides with the treasure  
    if pygame.sprite.spritecollide(goodG,treasureGrp,True):
       score = score + 1
       
# decrease the lives by one when the player collides with the bad guys 
    if pygame.sprite.spritecollide(goodG,badGuysGrp,False):
       lives = lives - 1
       x = 400 
       y = 685

# display loser screen when player lives is less than or equal 0    
    if lives <= 0:
      pygame.sprite.groupcollide(masterGrp,masterGrp,False,True)
          
      screen.fill((220,000,000))
      screen.blit(lose , (250, 400))
      
# display winner screen when player has 30 treasures     
    if score == 30:
      pygame.sprite.groupcollide(masterGrp,masterGrp,True,True)

      screen.fill((000,200,000))
      screen.blit(victory , (250, 400))     
       
# Move player when arrow key is pressed until player reaches the end of screen      
    if keys[K_UP] and y  > 15:
       y = y - 5
    
    if keys[K_LEFT] and x > 15:
       x = x - 5
    
    if keys[K_RIGHT] and x < 785:
       x = x + 5
    
    if keys [K_DOWN] and y < 685:
       y = y + 5
       
    
    
    
    
    
# update screen     
    pygame.display.flip()


    
    #Handle any events in the current frame
    for ev in pygame.event.get():

        if ev.type == QUIT: #<-- this special event type happens when the window is closed
            keepGoing = False

pygame.quit()  # Keep this IDLE friendly 