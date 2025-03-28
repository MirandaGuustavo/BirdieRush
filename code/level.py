import sys
import random

import pygame
from pygame import QUIT

from entity import Bird
from obstacle import Obstacle

class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entities = []
        self.bird = Bird(self.window)
        self.entities.append(self.bird)
        self.obstacles = []
        self.score = 0

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.window.fill((0, 0, 0))  # Limpa a tela

            self.handle_events()
            self.update_entities()
            self.render_entities()

            # Atualizar obstáculos
            self.spawn_obstacles()
            self.move_obstacles()

            pygame.display.flip()
            clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.bird.flap()

    def update_entities(self):
        self.bird.update()
        for obstacle in self.obstacles:
            obstacle.update()

    def render_entities(self):
        self.bird.render()
        for obstacle in self.obstacles:
            obstacle.render()

    def spawn_obstacles(self):
        if random.randint(1, 120) == 1:
            new_obstacle = Obstacle(self.window, self.window.get_width(), 300)
            self.obstacles.append(new_obstacle)

    def move_obstacles(self):
        for obstacle in self.obstacles[:]:
            obstacle.update()
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.score += 1