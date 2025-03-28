import pygame

class Obstacle:
    def __init__(self, window, x, gap_height):
        self.window = window
        self.width = 50
        self.gap = 300
        self.height_top = gap_height
        self.height_bottom = self.window.get_height() - (self.height_top + self.gap)
        self.x = x
        self.speed = 5
        self.rect_top = pygame.Rect(self.x, 0, self.width, self.height_top)
        self.rect_bottom = pygame.Rect(self.x, self.height_top + self.gap, self.width, self.height_bottom)
        self.passed = False

    def update(self, speed):
        self.x -= speed
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

    def draw(self):
        pygame.draw.rect(self.window, (0, 255, 0), self.rect_top)
        pygame.draw.rect(self.window, (0, 255, 0), self.rect_bottom)
