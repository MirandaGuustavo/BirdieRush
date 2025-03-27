import pygame
from menu import Menu
from game import Game

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))

    game = Game(window)
    menu = Menu(window)
    menu.show(game)

if __name__ == "__main__":
    main()

