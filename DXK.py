# -*- coding: utf-8 -*-
import pygame
class DXK(pygame.sprite.Sprite):
    def __init__(self, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture).convert_alpha()
        self.width, self.height = self.image.get_size()
        self.can_jump = True
        self.can_fly = False
        self.speed_x = 0
        self.speed_y = 0
        self.g = 0.02

    def jump(self, speed):
        if self.can_jump:
            self.can_jump = False
            self.speed_y = speed

    def land(self):
        self.can_jump = True
        self.speed_y = 0

    def move(self):
        self.speed_x = -2.5

    def fly(self):
        self.can_fly = True
        self.g = 0.015

    def stop(self):
        self.speed_x = 0
        self.can_fly = True
        self.g = 0.02

class Block(pygame.sprite.Sprite):
    def __init__(self, picture, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(picture).convert_alpha()
        self.width, self.height = self.image.get_size()
        self.x = x
        self.y = 500

    def __str__(self):
        return "Block(%.1f)"%self.x

    __repr__ = __str__

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]