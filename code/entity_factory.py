from entity import Bird
from obstacle import Obstacle


class EntityFactory:
    @staticmethod
    def create_bird(window):
        return Bird(window)

    @staticmethod
    def create_obstacle(window, x, y):
        return Obstacle(window, x, y)