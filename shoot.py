import pygame
from pygame import mixer
import random
import time
import math
import pygame.ftfont

from pygame.locals import *

pygame.init()
pygame.mixer.init()

# making a screen
screen= pygame.display.set_mode((800,600))
#changing the title and stuff
pygame.display.set_caption('Cosmic War1')

#background
bg= pygame.image.load('/home/spectrum93/Desktop/star/2.jpg')

#BGM
mixer.music.load('/home/spectrum93/Desktop/star/bgm.mp3')
mixer.music.play(-1)


icon = pygame.image.load('/home/spectrum93/Desktop/star/icon.png') #upload an icon soon..
pygame.display.set_icon(icon)

# defining the hero
playerimag = pygame.image.load('/home/spectrum93/Desktop/star/hero.png') #upload an image soon..
playerx=370
playery=480
playerx_change= 0
playery_change= 0


# defining the monster
monsterimg= []
monsterx=[]
monstery=[]
monsterx_change=[]
monstery_change= []
num_of_enemy = 6

for i in range(num_of_enemy):
    monsterimg.append(pygame.image.load('/home/spectrum93/Desktop/star/monster.png')) #upload an image soon..
    monsterx.append(random.randint(0, 730))
    monstery.append(random.randint(50,150))
    monsterx_change.append(2)
    monstery_change.append(30)

    
# defining the Bullet
# the bullet is currently moving
#ready -cant see the bullet on the screen
bulletimg = pygame.image.load('/home/spectrum93/Desktop/star/bullet.png') #upload an image soon..
bulletx=0
bullety= 480
bulletx_change= 0
bullety_change= 10
bullet_state ="ready"


#score sys

score=0
font= pygame.font.Font('freesansbold.ttf', 32)
text_x=10
text_y=10

# game over text
over= pygame.font.Font('freesansbold.ttf',84)



def show_score(x,y):
    s= font.render("SCORE:"+ str(score), True, (255,255,255))  
    screen.blit(s,(x,y))


def game_over():
    o= font.render("GAME OVER :/", True, (255,255,255))  
    screen.blit(o,(300, 250))



#player
def player(x, y):
    screen.blit(playerimag,(x , y))

#evil
def monster(x, y, i):
    screen.blit(monsterimg[i],(x , y))
# bullet fire
def fire_bullet(x ,y):
    global bullet_state
    bullet_state= "fire"
    screen.blit(bulletimg,(x + 16, y+ 10))

# about collision
def is_collision(monsterx, monstery, bulletx, bullety):
    distance= math.sqrt((math.pow(monsterx-bulletx,2))+(math.pow(monstery-bullety,2)) )
    if distance < 27:
        return True
    else :
        return False






#starting the window and the game loop
running = True
while running:
    
    screen.fill((0,0,0))    #background\
    #bg img
    screen.blit(bg, (0,0))

    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            running = False
    # checking the keystrokes
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
               playerx_change= -5
            if event.key == pygame.K_RIGHT:
                playerx_change= +5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                  # bullet_s= mixer.Sound('/home/spectrum93/Desktop/star/l.wav')
                  # bullet_s.play()                   
                   #gets the player position 
                   bulletx = playerx
                   fire_bullet(bulletx, bullety )    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerx_change= 0
    #player bound 
    playerx += playerx_change
    if playerx <=0:
        playerx_change =0
    elif playerx>=740:
        playerx_change=0

    

    #MONSter bound
    for i in range(num_of_enemy):
        
        #game over
        if monstery[i]> 440:
            for j in range(num_of_enemy):
                monstery[j]= 2000
            game_over()
            break 
        monsterx[i] += monsterx_change[i]
        if monsterx[i] <=0:
            monsterx_change[i] =4
            monstery[i]+= monstery_change[i]
        elif monsterx[i]>=740:
            monsterx_change[i]=-4 
            monstery[i] += monstery_change[i]
       # define collision
        collision = is_collision(monsterx[i], monstery[i], bulletx, bullety)
        if collision:
          #  explosion_s=mixer.Sound('/home/spectrum93/Desktop/star/e.wav')
          #  explosion_s.play()
                 
            bullety = 480
            bullet_state ="ready"
            score += 1
            monsterx[i]=random.randint(0, 730)
            monstery[i]=random.randint(50,150)

        monster(monsterx[i], monstery[i], i)
    
    
    #bullet movement'

    if bullety <= 0:
        bullet_state ="ready"
        bullety = 480   
    if bullet_state is "fire":
        fire_bullet(bulletx, bullety)
        bullety -= bullety_change
    #collision

    
    player(playerx, playery)
    show_score(text_x, text_y)
    pygame.display.update()
