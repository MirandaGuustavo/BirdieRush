import pygame

class Bird:
    def __init__(self, window):
        self.window = window
        self.x = 100
        self.y = 200
        self.width = 50
        self.height = 50
        self.gravity = 1
        self.velocity = 0
        self.lift = -12
        self.image_index = 0
        self.images = self.load_images()
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.jump_sound = pygame.mixer.Sound("../assets/jump.mp3")

    def load_images(self):
        images = []
        for i in range(1, 5):
            image = pygame.image.load(f"../assets/bird{i}.png")  # Ajuste para os arquivos PNG
            image = pygame.transform.scale(image, (self.width, self.height))  # Redimensiona a imagem
            images.append(image)
        return images

    def update(self, min_height, max_height, safe_margin=10):

        self.velocity += self.gravity
        self.y += self.velocity
        self.rect.y = self.y

        # limitar o movimento do pássaro dentro da tela
        if self.rect.top < min_height:
            self.rect.top = min_height
            self.y = min_height

        if self.rect.bottom > max_height + safe_margin:
            self.rect.bottom = max_height + safe_margin  # Limite inferior ajustado
            self.y = max_height + safe_margin - self.height  # Evita ultrapassar o limite inferior

    def jump(self):
        self.velocity = self.lift
        self.jump_sound.play()

    def draw(self):
        self.window.blit(self.images[self.image_index], (self.x, self.y))
        self.image_index = (self.image_index + 1) % 4
