import pygame

class Obstacle:
    def __init__(self, window, x, gap_height):
        self.window = window
        self.width = 50  # Largura dos obstáculos
        self.gap = 300  # Espaçamento mínimo entre os obstáculos
        self.height_top = gap_height  # Altura do topo do obstáculo
        self.height_bottom = self.window.get_height() - (self.height_top + self.gap)  # Garantir o espaçamento
        self.x = x  # Posição inicial dos obstáculos
        self.speed = 5  # Velocidade dos obstáculos
        self.rect_top = pygame.Rect(self.x, 0, self.width, self.height_top)  # Parte superior do obstáculo
        self.rect_bottom = pygame.Rect(self.x, self.height_top + self.gap, self.width, self.height_bottom)  # Parte inferior
        self.passed = False  # Indica se o obstáculo já foi ultrapassado pelo pássaro

    def update(self, speed):
        self.x -= speed
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), self.rect_top)  # Desenha o topo do obstáculo
        pygame.draw.rect(self.window, (0, 255, 0), self.rect_bottom)  # Desenha a parte inferior do obstáculo
