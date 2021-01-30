# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 20:25:59 2021

@author: Ian B
"""

import pygame
# import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

WIDTH = 1024
HEIGHT = 768
FPS = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Player1.png").convert()
        self.image.set_colorkey(BLACK)
        # self.image = pygame.Surface((50,50))
        # self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.y_move = 5
        
        
        
        
        
    def update(self):
        self.rect.x += 5 
        self.rect.y += self.y_move
        
        if self.rect.left > WIDTH:
            self.rect.right = 0
            
        if self.rect.bottom > HEIGHT -200:
            self.y_move = -5
        
        if self.rect.top < 200:
            self.y_move = 5
            
        if self.rect.left > WIDTH:
            self.rect.right = 0



#initiaalise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Boing!")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#game loop
running = True

while running:
    
    clock.tick(FPS)
    
    #process input
    for event in pygame.event.get():
        
        if event.type ==  pygame.QUIT:
            running = False
    
    #update
    
    all_sprites.update()
    
    #render/ draw
    
    screen.fill(GREEN)
    all_sprites.draw(screen)
    
    pygame.display.flip()
    # pygame.display.update()

pygame.quit()
