import pygame
from menu import Menu
from game import Game

def main():
    pygame.init()
    window = pygame.display.set_mode((800, 600))  # Criando a janela do jogo

    game = Game(window)  # Inicializa o jogo
    menu = Menu(window)  # Inicializa o menu
    menu.show(game)  # Passa o objeto do jogo para o menu e exibe o menu

if __name__ == "__main__":
    main()

