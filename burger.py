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
burger1 = pygame.image.load("photos/burger.png").convert_alpha()

class BURGER:
    def __init__(self):
        #create an x and y position
        #draw a square
        self.randomize()
    def draw_burger(self):
        #create a rectangle 
        # draw a rectangle
        fruit_rect = pygame.Rect(int(self.x*cell_size),int(self.y*cell_size),cell_size,cell_size)
        # pygame.draw.rect(screen,(126,166,114),fruit_rect)
        screen.blit(burger1,fruit_rect)
    def randomize(self):
        self.x = random.randint(0,cell_number-1)
        self.y = random.randint(0,cell_number-1)
        self.pos = Vector2(self.x,self.y)