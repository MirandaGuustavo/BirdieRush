import pygame
from menu import Menu
from game import Game

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))

    menu = Menu(window)

    while True:
        game = Game(window)
        menu.show(game)
        game.run()

if __name__ == "__main__":
    main()
