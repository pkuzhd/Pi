background_image_filename = 'sushiplate.jpg'
mouse_image_filename = 'fugu.png'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

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
                    screen = pygame.display.set_mode((1024, 768), FULLSCREEN | HWSURFACE, 32)
                else:
                    screen = pygame.display.set_mode((640, 480), 0, 32)
        if event.type == KEYDOWN:
            if event.key == 285 and event.mod == 256:
                exit()

    if Fullscreen:
        screen.blit(background, (192,144))
    else:
        screen.blit(background, (0,0))
    x, y = pygame.mouse.get_pos()
    #获得鼠标位置
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    #计算光标的左上角位置
    screen.blit(mouse_cursor, (x, y))
    #把光标画上去
    pygame.display.update()
