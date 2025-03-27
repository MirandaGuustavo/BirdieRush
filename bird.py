import pygame

class Bird:
    def __init__(self, window):
        self.window = window
        self.x = 100  # Posição inicial do pássaro
        self.y = 200  # Posição inicial do pássaro
        self.width = 50  # Largura ajustada do pássaro
        self.height = 50  # Altura ajustada do pássaro
        self.gravity = 1  # Força da gravidade
        self.velocity = 0  # Velocidade do pássaro (inicialmente sem movimento vertical)
        self.lift = -12  # Força do pulo (subida)
        self.image_index = 0  # Controla qual frame do pássaro está sendo usado
        self.images = self.load_images()  # Carregar as imagens do pássaro
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)  # A posição e colisão do pássaro

    def load_images(self):
        """Carregar as 4 imagens do pássaro."""
        images = []
        for i in range(1, 5):
            image = pygame.image.load(f"assets/bird{i}.png")  # Ajuste para os arquivos PNG
            image = pygame.transform.scale(image, (self.width, self.height))  # Redimensiona a imagem
            images.append(image)
        return images

    def update(self, min_height, max_height, safe_margin=10):
        """Atualiza o movimento do pássaro com gravidade e a capacidade de pular, respeitando os limites."""
        self.velocity += self.gravity  # Aplica a gravidade
        self.y += self.velocity  # Move o pássaro para baixo
        self.rect.y = self.y  # Atualiza a posição do retângulo para colisão

        # Limitar o movimento do pássaro dentro da tela (sem ultrapassar os limites superior e inferior)
        if self.rect.top < min_height:
            self.rect.top = min_height  # Limite superior
            self.y = min_height

        # Ajustar o limite inferior, permitindo um deslocamento um pouco abaixo da borda
        if self.rect.bottom > max_height + safe_margin:
            self.rect.bottom = max_height + safe_margin  # Limite inferior ajustado
            self.y = max_height + safe_margin - self.height  # Evita ultrapassar o limite inferior

    def jump(self):
        """Faz o pássaro saltar, ajustando a velocidade para um pulo."""
        self.velocity = self.lift  # Quando o pulo é ativado, a velocidade é ajustada para a força do pulo

    def draw(self):
        """Desenha o pássaro na tela com animação."""
        self.window.blit(self.images[self.image_index], (self.x, self.y))
        self.image_index = (self.image_index + 1) % 4  # Controla a animação do pássaro (ciclo de 4 imagens)
