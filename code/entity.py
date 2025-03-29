import pygame

class Entity:
    def __init__(self, window, image_path, x, y):
        self.window = window
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        pass

    def render(self):
        self.window.blit(self.image, self.rect)

class Bird(Entity):
    def __init__(self, window):
        super().__init__(window, 'assets/bird.png', 100, 300)
        self.velocity = 0
        self.gravity = 0.5
        self.lift = -15

    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity

    def flap(self):
        self.velocity = self.lift