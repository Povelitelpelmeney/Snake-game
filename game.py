import pygame,sys,random
from pygame.math import Vector2
from lava import LAVA
from fruit import FRUIT
from snake import SNAKE
from speed_fruit import S_FRUIT
from burger import BURGER

pygame.init()
cell_size=40
cell_number=20
screen  = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load("photos/apple.png").convert_alpha()
s_apple = pygame.image.load("photos/g_apple.png").convert_alpha()
burger1 = pygame.image.load("photos/burger.png").convert_alpha()
lava1 = pygame.image.load("photos/lava.png").convert_alpha()
game_font = pygame.font.Font("fonts/PoetsenOne-Regular.ttf",25)

class MAIN(SNAKE,FRUIT,LAVA):
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.s_fruit = []
        self.lava = [LAVA()]
        self.diff = 1
        self.burger = []
        self.lives=2
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        for el in self.burger:
            el.draw_burger()
        for el in self.s_fruit:
            el.draw_s_fruit()
        self.snake.draw_snake()
        for lav in self.lava:
            lav.draw_lava()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos==self.snake.body[0]:
            self.fruit.randomize()
            while True:
                sch=0
                for lav in self.lava:
                    if self.fruit.x==lav.x and self.fruit.y==lav.y:
                        self.fruit.randomize()
                        sch+=1
                for block in self.snake.body[1:]:
                    if block==self.fruit.pos:
                        self.fruit.randomize()
                        sch+=1
                for el in self.s_fruit:
                    if el.pos == self.fruit.pos:
                        self.fruit.randomize()
                        sch+=1
                for el in self.burger:
                    if el.pos == self.fruit.pos:
                        self.fruit.randomize()
                        sch+=1
                if sch==0:
                    break
            self.snake.add_block(1)
            self.snake.play_crunch_sound()
            for i in range(int(self.diff)):
                new_lava = LAVA()
                self.lava.append(new_lava)
                self.lava[-1].randomize()
                while True:
                    sch=0
                    lav=self.lava[-1]
                    for i in range(len(self.lava)-2):
                        if self.lava[i].x==lav.x and self.lava[i].y==lav.y:
                            self.lava[-1].randomize()
                            sch+=1
                    for block in self.snake.body[1:]:
                        if block.x==lav.x and block.y==lav.y:
                            self.lava[-1].randomize()
                            sch+=1
                    for el in self.s_fruit:
                        if el.x == lav.x and el.y==lav.y:
                            self.lava[-1].randomize()
                            sch+=1
                    for el in self.burger:
                        if el.pos == lav.pos:
                            self.lava[-1].randomize()
                            sch+=1
                    if sch==0:
                        break
            if len(self.snake.body)%5==0:
                new_s_apple=S_FRUIT()
                self.s_fruit.append(new_s_apple)
                self.s_fruit[-1].randomize()
                while True:
                    sch=0
                    for i in range(len(self.lava)-1):
                        if self.s_fruit[-1].pos==self.lava[i].pos:
                            self.s_fruit[-1].randomize()
                            sch+=1
                    for block in self.snake.body[1:]:
                        if block.x==self.s_fruit[-1].x and block.y==self.s_fruit[-1].y:
                            self.s_fruit[-1].randomize()
                            sch+=1
                    for el in range(len(self.s_fruit)-2):
                        if self.s_fruit[el].pos==self.s_fruit[-1].pos:
                            self.s_fruit[-1].randomize()
                            sch+=1
                    for block in self.burger:
                        if block.pos==self.s_fruit[-1].x:
                            self.s_fruit[-1].randomize()
                            sch+=1
                    if sch==0:
                        break
            if len(self.snake.body)%10==0:
                burger = BURGER()
                self.burger.append(burger)
                self.burger[-1].randomize()
                while True:
                    sch=0
                    for i in range(len(self.lava)-1):
                        if self.burger[-1].pos==self.lava[i].pos:
                            self.burger[-1].randomize()
                            sch+=1
                    for block in self.snake.body[1:]:
                        if block.x==self.burger[-1].x and block.y==self.burger[-1].y:
                            self.burger[-1].randomize()
                            sch+=1
                    for el in self.s_fruit:
                        if el.pos==self.burger[-1].pos:
                            self.burger[-1].randomize()
                            sch+=1
                    if sch==0:
                        break
            #reposition fruit
            #add length to snake
        for lav in self.lava:
            if lav.pos == self.snake.body[0]:
                if self.lives>0:
                    self.snake.delete_block()
                    self.lives-=1
                else:
                    self.game_over()
        for el in self.s_fruit:
            if el.pos == self.snake.body[0]:
                self.snake.add_speed()
                self.snake.add_block(1)
                self.snake.play_crunch_sound()
                self.s_fruit.remove(el)
        for el in self.burger:
            if self.snake.body[0]==el.pos:
                self.snake.add_block(3)
                self.snake.play_crunch_sound()
                self.burger.remove(el)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def draw_grass(self):
        grass_color=(167,209,61)
        for row in range(cell_number):
            if row%2==0:
                for column in range(cell_number):
                    if column%2==0:
                        grass_rect=pygame.Rect(column*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for column in range(cell_number):
                    if column%2!=0:
                        grass_rect=pygame.Rect(column*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
    def draw_score(self):
        score_text = str(len(self.snake.body)-3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        screen.blit(score_surface,score_rect)
        
    def game_over(self):
        pygame.quit()
        sys.exit()()