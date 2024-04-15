import pygame
import pygame_menu
from main import main_function
from save_parser import parser

pygame.init()
diff = 1


def change_difficulty(value, difficulty):
    global diff
    global button1
    global button2
    global button3
    diff = difficulty
    menu.remove_widget(button1)
    menu.remove_widget(button2)
    menu.remove_widget(button3)
    pars = parser()
    button1 = menu.add.button('Play', main_function, diff)
    button2 = menu.add.button('Save_load', main_function, pars.diff, pars)
    button3 = menu.add.button('Quit', pygame_menu.events.EXIT)


surface = pygame.display.set_mode((800, 800))


def menu_funcion():
    global menu
    global button1
    global button2
    global button3
    pars = parser()
    menu = pygame_menu.Menu('Snake', 800, 800,
                            theme=pygame_menu.themes.THEME_GREEN)
    menu.add.selector('difficulty', [('easy', 1), ('medium', 2), ('hard', 3)],
                      onchange=change_difficulty,
                      style='fancy', style_fancy_arrow_margin=(0, 0, 0),
                      style_fancy_bgcolor=(0, 0, 0, 0),
                      style_fancy_bordercolor=(0, 0, 0, 0),
                      style_fancy_arrow_color=(220, 132, 201))
    button1 = menu.add.button('Play', main_function, diff)
    button2 = menu.add.button('Save_load', main_function, pars.diff, pars)
    button3 = menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)
