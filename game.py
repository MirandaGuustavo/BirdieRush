import pygame
import random
from bird import Bird
from obstacle import Obstacle


class Game:
    def __init__(self, window):
        self.window = window
        self.clock = pygame.time.Clock()
        self.bird = Bird(self.window)  # Criando o pássaro
        self.obstacles = []
        self.game_over = False
        self.score = 0
        self.obstacle_gap = 250  # Distância inicial entre os obstáculos
        self.min_height = 0  # Limite superior da tela
        self.max_height = self.window.get_height() + 70  # Limite inferior da tela
        self.obstacle_speed = 5  # Velocidade inicial dos obstáculos

    def run(self):
        while not self.game_over:
            self.window.fill((255, 255, 255))  # Limpa a tela

            # Lógica de movimento do pássaro
            self.bird.update(self.min_height, self.max_height)

            # Geração e movimentação dos obstáculos
            self.create_obstacles()
            self.move_obstacles()

            # Verificar colisões
            self.check_collisions()

            # Exibir o score
            self.display_score()

            # Desenhar o pássaro e os obstáculos
            self.bird.draw()
            for obstacle in self.obstacles:
                obstacle.draw()

            # Atualizar a tela
            pygame.display.flip()

            # Controlar a taxa de quadros por segundo (FPS)
            self.clock.tick(60)

            # Aumentar a dificuldade conforme o tempo ou pontos
            self.increase_difficulty()

            # Verificar eventos de teclado e sair do jogo
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()  # Chama o metodo de pulo ao pressionar a tecla space

    def create_obstacles(self):
        # Gera um novo obstáculo apenas se não houver ou se o último estiver distante o suficiente
        if len(self.obstacles) == 0 or self.obstacles[-1].x < self.window.get_width() - 250:
            obstacle_x = self.window.get_width()  # Faz o obstáculo aparecer fora da tela
            obstacle_y = random.randint(100, self.window.get_height() - 100)  # Posição aleatória na altura

            self.obstacles.append(Obstacle(self.window, obstacle_x, obstacle_y))

    def move_obstacles(self):
        for obstacle in self.obstacles:
            obstacle.update(self.obstacle_speed)  # Passa a velocidade dos obstáculos para o metodo update

        # Remover obstáculos fora da tela
        self.obstacles = [obstacle for obstacle in self.obstacles if obstacle.x > -50]

    def check_collisions(self):
        """Verifica se o pássaro colide com os obstáculos"""
        for obstacle in self.obstacles:
            if self.bird.rect.colliderect(obstacle.rect_top) or self.bird.rect.colliderect(obstacle.rect_bottom):
                self.game_over = True  # Fim do jogo em caso de colisão

    def display_score(self):
        font = pygame.font.SysFont('Arial', 24)
        score_text = font.render(f"Score: {self.score}", True, (0, 0, 0))
        self.window.blit(score_text, (10, 10))

    def increase_difficulty(self):
        """Aumenta a velocidade dos obstáculos e reduz o espaçamento conforme o tempo ou a pontuação."""
        if self.score % 100 == 0:  # Aumenta a cada 100 pontos
            self.obstacle_speed += 1  # Aumenta a velocidade dos obstáculos
            self.score += 1  # Impede que a dificuldade aumente várias vezes no mesmo intervalo
