import pygame


class ParallaxBackground:
    def __init__(self, window, image_paths, speeds):
        self.window = window
        self.layers = []
        self.screen_width = window.get_width()
        self.screen_height = window.get_height()

        # carregar as imagens e configurar as posições iniciais
        for i, path in enumerate(image_paths):
            image = pygame.image.load(path).convert_alpha()
            width = image.get_width()
            height = image.get_height()

            # ajusta a largura da imagem para o tamanho da tela
            if width > self.screen_width:
                height = int(height * (self.screen_width / width))
                width = self.screen_width
            if height < self.screen_height:
                height = self.screen_height
                image = pygame.transform.scale(image, (width, height))
            else:
                image = pygame.transform.scale(image, (width, height))

            # criando duas vezes as imagens para o efeito de loop contínuo
            self.layers.append({
                "image": image,
                "x1": 0,
                "x2": width,
                "speed": speeds[i],
                "width": width,
                "height": height
            })
            self.layers.append({
                "image": image,
                "x1": width,
                "x2": width * 2,
                "speed": speeds[i],
                "width": width,
                "height": height
            })

    def update(self):
        for layer in self.layers:
            layer["x1"] -= layer["speed"]
            layer["x2"] -= layer["speed"]

            # reinicia a posição das camadas
            if layer["x1"] <= -layer["width"]:
                layer["x1"] = layer["x2"] + layer["width"]
            if layer["x2"] <= -layer["width"]:
                layer["x2"] = layer["x1"] + layer["width"]

    def draw(self):
        for layer in self.layers:
            self.window.blit(layer["image"], (layer["x1"], 0))
            self.window.blit(layer["image"], (layer["x2"], 0))
