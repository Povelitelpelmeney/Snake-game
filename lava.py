import pygame,sys,random
from pygame.math import Vector2

pygame.init()
cell_size=40
cell_number=20
screen  = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("photos/apple.png").convert_alpha()
s_apple = pygame.image.load("photos/g_apple.png").convert_alpha()
lava1 = pygame.image.load("photos/lava.png").convert_alpha()
game_font = pygame.font.Font("fonts/PoetsenOne-Regular.ttf",25)

class LAVA:
    def __init__(self):
        #create an x and y position
        #draw a square
        self.randomize()
    def draw_lava(self):
        #create a rectangle 
        # draw a rectangle
        lava_rect = pygame.Rect(int(self.x*cell_size-cell_size*0.36),int(self.y*cell_size-cell_size*0.36),cell_size,cell_size)
        # pygame.draw.rect(screen,(126,166,114),lava_rect)
        screen.blit(lava1,lava_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)