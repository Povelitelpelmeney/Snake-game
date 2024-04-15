from game import MAIN
from speed_fruit import S_FRUIT
from lava import LAVA
from burger import BURGER
from snake import SNAKE
from pygame.math import Vector2


def parser():
    with open('save.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        main = MAIN()
        arr = data.split("#")
        # ///////////snake
        snakey = SNAKE()
        arr_snake = arr[0].split("$")
        arr_snake_pos = []
        for i in range(len(arr_snake[0])):
            if arr_snake[0][i] == "(":
                sch = 2
                x = arr_snake[0][i + 1]
                while arr_snake[0][i + sch] != ",":
                    x += arr_snake[0][i + sch]
                    sch += 1
                sch += 1
                x = int(x)
                y = arr_snake[0][i + sch]
                while arr_snake[0][i + sch + 1] != ")":
                    y += arr_snake[0][i + sch + 1]
                    sch += 1
                y = int(y)
                vec = Vector2(x, y)
                arr_snake_pos.append(vec)
        snakey.body = arr_snake_pos
        arr_snake_direction = arr_snake[1].split(",")
        snakey.direction = Vector2(int(arr_snake_direction[0][1:]),
                                   int(arr_snake_direction[1][:-1]))
        snakey.speed = int(arr_snake[2])
        main.snake = snakey
        # ///////////fruit
        arr_fruit = arr[1].split("$")
        main.fruit.x = int(arr_fruit[0])
        main.fruit.y = int(arr_fruit[1])
        main.fruit.pos = Vector2(main.fruit.x, main.fruit.y)
        # ///////////s_fruit
        arr_s_fruit = arr[2].split(",")
        arr_main_s_fruit = []
        for i in range(len(arr_s_fruit)):
            for j in range(len(arr_s_fruit[i])):
                if arr_s_fruit[i][j] == "'" and j < len(arr_s_fruit[i]) - 2:
                    sch = 2
                    x = arr_s_fruit[i][j + 1]
                    while arr_s_fruit[i][j + sch] != "$":
                        x += arr_s_fruit[i][j + sch]
                        sch += 1
                    sch += 1
                    x = int(x)
                    y = ""
                    while arr_s_fruit[i][j + sch] != "'":
                        y += arr_s_fruit[i][j + sch]
                        sch += 1
                    y = int(y)
                    vec = Vector2(x, y)
                    sfr = S_FRUIT()
                    sfr.pos = vec
                    sfr.x = int(vec.x)
                    sfr.y = int(vec.y)
                    arr_main_s_fruit.append(sfr)
        main.s_fruit = arr_main_s_fruit
        # ///////////lava
        arr_lava = arr[3].split(",")
        arr_main_lava = []
        for i in range(len(arr_lava)):
            for j in range(len(arr_lava[i])):
                if arr_lava[i][j] == "'" and j < len(arr_lava[i]) - 2:
                    sch = 2
                    x = arr_lava[i][j + 1]
                    while arr_lava[i][j + sch] != "$":
                        x += arr_lava[i][j + sch]
                        sch += 1
                    sch += 1
                    x = int(x)
                    y = ''
                    while arr_lava[i][j + sch] != "'":
                        y += arr_lava[i][j + sch]
                        sch += 1
                    y = int(y)
                    vec = Vector2(x, y)
                    lav = LAVA()
                    lav.pos = vec
                    lav.x = int(vec.x)
                    lav.y = int(vec.y)
                    arr_main_lava.append(lav)
        main.lava = arr_main_lava
        # ///////////diff
        main.diff = int(arr[4])
        # ///////////burger
        arr_burg = arr[5].split(",")
        arr_main_burg = []
        for i in range(len(arr_burg)):
            for j in range(len(arr_burg[i])):
                if arr_burg[i][j] == "'" and j < len(arr_burg[i]) - 2:
                    sch = 2
                    x = arr_burg[i][j + 1]
                    while arr_burg[i][j + sch] != "$":
                        x += arr_burg[i][j + sch]
                        sch += 1
                    sch += 1
                    x = int(x)
                    y = ''
                    while arr_burg[i][j + sch] != "'":
                        y += arr_burg[i][j + sch]
                        sch += 1
                    y = int(y)
                    vec = Vector2(x, y)
                    burger = BURGER()
                    burger.pos = vec
                    burger.x = int(vec.x)
                    burger.y = int(vec.y)
                    arr_main_burg.append(burger)
        main.burger = arr_main_burg
        # ///////////lives
        main.lives = int(arr[6])
        # ///////////level
        main.level = int(arr[7])
        # ///////////in_game
        main.in_game = int(arr[8])
        return main
