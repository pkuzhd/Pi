background_image_filename = 'sushiplate.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
 
Fullscreen = False
print(pygame.display.list_modes())
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_f:
                Fullscreen = not Fullscreen
                if Fullscreen:
                    screen = pygame.display.set_mode((1366, 768), FULLSCREEN | HWSURFACE, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
        if event.type == KEYDOWN:
            if event.key == 285 and event.mod == 256:
                exit()

    if Fullscreen:
        screen.blit(background, (363,144))
    else:
        screen.blit(background, (0,0))
    
    pygame.display.update()