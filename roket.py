import pygame
import time
import os

pygame.font.init()
pygame.mixer.init()

# VARIBLE # 
high = 500
wight = 900
WHITE = (225, 225, 225)
black = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
border = pygame.Rect(wight//2 - 5, 0, 10, high)
bullet_hit_sound = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))
bullet_fire_sound = pygame.mixer.Sound(os.path.join('Assets', 'gun+silencer.mp3'))


HEALTH_FOND = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
FPS = 60
vel = 5
bullet_vel = 7
max_bullets = 3

yellow_hit = pygame.USEREVENT + 1
red_hit = pygame.USEREVENT + 2

yellow_spaceship_image = pygame.image.load('Assets\spaceship_yellow.png')
yellow_spaceship = pygame.transform.rotate(pygame.transform.scale(yellow_spaceship_image, (55, 40)), 90)
red_spaceship_image = pygame.image.load('Assets\spaceship_red.png')
red_spaceship = pygame.transform.rotate(pygame.transform.scale(red_spaceship_image, (55, 40)), 270)

space = pygame.transform.scale(pygame.image.load(os.path.join('Assets', 'space.png')), (wight, high))



main_scrin = pygame.display.set_mode((wight, high))
pygame.display.set_caption("ROKET GAME")

def draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    main_scrin.blit(space, (0, 0))
    pygame.draw.rect(main_scrin, black, border)

    red_health_text = HEALTH_FOND.render("health:" + str(red_health), 1, WHITE)
    yellow_health_text = HEALTH_FOND.render("health:" + str(yellow_health), 1, WHITE)
    main_scrin.blit(red_health_text, (wight - red_health_text.get_width() - 10, 10))
    main_scrin.blit(yellow_health_text, (10, 10) )
    main_scrin.blit(yellow_spaceship, (yellow.x ,yellow.y))
    main_scrin.blit(red_spaceship, (red.x, red.y))

    
    for bullet in red_bullets:
          pygame.draw.rect(main_scrin, RED, bullet)

    for bullet in yellow_bullets:
          pygame.draw.rect(main_scrin, YELLOW, bullet)

    pygame.display.update()


def yellow_handel_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_d] and yellow.x - vel < 400: # RIGHT
            yellow.x += vel
    if keys_pressed[pygame.K_a] and yellow.x + vel > 0: #LEFT
            yellow.x -= vel    
    if keys_pressed[pygame.K_w] and yellow.y - vel > 0: # UP
            yellow.y -= vel
    if keys_pressed[pygame.K_s] and yellow.y + vel < 450: #DOWN
            yellow.y += vel 


def red_handel_movement(keys_pressed, red):
    if keys_pressed[pygame.K_RIGHT] and red.x + vel < 865: # RIGHT
            red.x += vel
    if keys_pressed[pygame.K_LEFT] and red.x - vel > 450: #LEFT
            red.x -= vel    
    if keys_pressed[pygame.K_UP] and red.y - vel > 0: # UP
            red.y -= vel
    if keys_pressed[pygame.K_DOWN] and red.y + vel < 450: #DOWN
            red.y += vel


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
      for bullet in yellow_bullets:
            bullet.x += bullet_vel
            if red.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(red_hit))
                  yellow_bullets.remove(bullet)
            elif bullet.x > wight:
                  yellow_bullets.remove(bullet)      

      for bullet in red_bullets:
            bullet.x -= bullet_vel
            if yellow.colliderect(bullet):
                  pygame.event.post(pygame.event.Event(yellow_hit))
                  red_bullets.remove(bullet)
            elif bullet.x < 0:
                  red_bullets.remove(bullet)        


def draw_winner(text):
      draw_text = WINNER_FONT.render(text, 1, WHITE)
      main_scrin.blit(draw_text, (wight/2 - draw_text.get_width()/2, high/2 - draw_text.get_height()/2))
      pygame.display.update()
      pygame.time.delay(5000)


def main():
    yellow = pygame.Rect(100, 200 ,55 ,40)
    red = pygame.Rect(800, 200, 55 ,40)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < max_bullets:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                    bullet_fire_sound.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) < max_bullets:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    bullet_fire_sound.play()

            if event.type == red_hit:
              red_health -= 1
              bullet_hit_sound.play()

            if event.type == yellow_hit:
              yellow_health -= 1
              bullet_hit_sound.play()

        winner_text = ""
        if red_health <= 0:
              winner_text = "yellow winner!"
              
        if yellow_health <= 0:
              winner_text = "red winner!"

        if winner_text != "":
              draw_winner(winner_text)
              break     
                    
                           
        
        
        keys_pressed = pygame.key.get_pressed()
        yellow_handel_movement(keys_pressed, yellow)
        red_handel_movement(keys_pressed, red)   

        handle_bullets(yellow_bullets, red_bullets, yellow, red)
        
        draw_window(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)        

    main()           

if __name__ == "__main__":
    main()    