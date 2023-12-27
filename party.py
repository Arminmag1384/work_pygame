import pygame
import sys
import time
import random

pygame.init()

# VARIBLES #
high = 1024
wight = 1950
color = "red"

# ____ #

main_scren = pygame.display.set_mode((wight, high))

# GAMR TIMER #
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                color = "blue"
            if event.key == pygame.K_a:
                color = "red"
    circleX = random.randrange(50, 1900)
    circleY = random.randrange(50, 9950)
    radius = random.randrange(40, 60)
    pygame.draw.circle(main_scren, color, (circleX, circleY), radius)

    if color == "red":    
        color = "green" 
            
    elif color == "green":
        color = "red"  
        
    elif color == "blue":
        color = "yellow"

    else:
        color = "blue"   

    pygame.display.update() 
    clock.tick(5)       
