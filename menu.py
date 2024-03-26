import pygame
import pygame_menu
from main import main_function

pygame.init()
diff=1
def change_difficulty(value,difficulty):
    global diff
    global button1
    global button2
    diff=difficulty
    menu.remove_widget(button1)
    menu.remove_widget(button2)
    button1=menu.add.button('Play', start_the_game,diff)
    button2=menu.add.button('Quit', pygame_menu.events.EXIT)
surface = pygame.display.set_mode((800, 800), pygame.FULLSCREEN)
def start_the_game(diff):
    main_function(diff)

menu = pygame_menu.Menu('Snake', 800, 800,
                    theme=pygame_menu.themes.THEME_GREEN)
menu.add.selector('difficulty', [('easy', 1), ('medium', 2), ('hard', 3)], onchange=change_difficulty, style='fancy', style_fancy_arrow_margin=(0, 0, 0), style_fancy_bgcolor=(0, 0, 0, 0), style_fancy_bordercolor=(0, 0, 0, 0), style_fancy_arrow_color=(220, 132, 201))
button1=menu.add.button('Play', start_the_game,diff)
button2=menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(surface)