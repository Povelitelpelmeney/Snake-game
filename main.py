import pygame
import sys
import random
from pygame.math import Vector2
from game import MAIN
from save_loader import loader


def main_function(diff, obj=0):
    pygame.init()
    cell_size = 40
    cell_number = 20
    screen = pygame.display.set_mode((cell_number * cell_size,
                                      cell_number * cell_size))
    clock = pygame.time.Clock()
    if obj == 0:
        main_game = MAIN()
    else:
        main_game = obj
    main_game.diff = diff
    info = main_game.display_info()
    loader(info)
    apple = pygame.image.load("photos/apple.png").convert_alpha()
    heart = pygame.image.load("photos/heart.png").convert_alpha()
    s_apple = pygame.image.load("photos/g_apple.png").convert_alpha()
    lava1 = pygame.image.load("photos/lava.png").convert_alpha()
    burger1 = pygame.image.load("photos/burger.png").convert_alpha()
    game_font = pygame.font.Font("fonts/PoetsenOne-Regular.ttf", 25)
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 0)
    music_choice = random.randint(1, 3)
    temp_music = pygame.mixer.Sound(f"sounds/music/{music_choice}.mp3")
    temp_music.play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                info = main_game.display_info()
                loader(info)
                for i in range(len(main_game.timers)):
                    main_game.timers[i].cancel()
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.time.set_timer(SCREEN_UPDATE,
                                          main_game.snake.speed)
                if event.key == pygame.K_UP:
                    if main_game.snake.direction.y != 1:
                        main_game.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_RIGHT:
                    if main_game.snake.direction.x != -1:
                        main_game.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_DOWN:
                    if main_game.snake.direction.y != -1:
                        main_game.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_LEFT:
                    if main_game.snake.direction.x != 1:
                        main_game.snake.direction = Vector2(-1, 0)
        if main_game.level % 4 == 0:
            screen.fill((175, 215, 70))
        elif main_game.level % 4 == 1:
            screen.fill((255, 165, 0))
        elif main_game.level % 4 == 2:
            screen.fill((255, 215, 0))
        elif main_game.level % 4 == 3:
            screen.fill((175, 238, 238))
        if len(main_game.snake.body) >= 10 and main_game.level < 1:
            main_game.level = 1
        if len(main_game.snake.body) >= 15 and main_game.level < 2:
            main_game.level = 2
        if len(main_game.snake.body) >= 20:
            main_game.level = 3
        main_game.draw_elements()
        if main_game.in_game == 0:
            temp_music.stop()
            break

        # draw all our elements
        pygame.display.update()
        clock.tick(120)
