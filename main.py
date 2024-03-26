import pygame,sys,random
from pygame.math import Vector2
from lava import LAVA
from fruit import FRUIT
from snake import SNAKE
from game import MAIN
from burger import BURGER


def main_function(diff):
    pygame.init()
    cell_size=40
    cell_number=20
    screen  = pygame.display.set_mode((cell_number*cell_size,cell_number*cell_size))
    clock = pygame.time.Clock()
    main_game = MAIN()
    main_game.diff = diff
    apple = pygame.image.load("photos/apple.png").convert_alpha()
    s_apple = pygame.image.load("photos/g_apple.png").convert_alpha()
    lava1 = pygame.image.load("photos/lava.png").convert_alpha()
    burger1 = pygame.image.load("photos/burger.png").convert_alpha()
    game_font = pygame.font.Font("fonts/PoetsenOne-Regular.ttf",25)

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE,100)
    music_choice=random.randint(1,3)
    temp_music=pygame.mixer.Sound(f"sounds/music/{music_choice}.mp3")
    temp_music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y!=1:
                        main_game.snake.direction = Vector2(0,-1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x!=-1:
                        main_game.snake.direction = Vector2(1,0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y!=-1:
                        main_game.snake.direction = Vector2(0,1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x!=1:
                        main_game.snake.direction = Vector2(-1,0)
        screen.fill((175,215,70))
        main_game.draw_elements()
        #draw all our elements
        pygame.display.update()
        clock.tick(120)
