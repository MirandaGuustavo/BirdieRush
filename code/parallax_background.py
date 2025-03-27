import pygame


class ParallaxBackground:
    def __init__(self, window, image_paths, speeds):
        self.window = window
        self.layers = []
        self.screen_width = window.get_width()
        self.screen_height = window.get_height()

        # Carregar as imagens e configurar as posições iniciais
        for i, path in enumerate(image_paths):
            image = pygame.image.load(path).convert_alpha()  # Carregar imagem com transparência
            width = image.get_width()
            height = image.get_height()


            if height < self.screen_height:
                height = self.screen_height
                image = pygame.transform.scale(image, (width, height))

            # Criando duas vezes as imagens para o efeito de loop contínuo
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
        # Move as camadas para criar o efeito de parallax
        for layer in self.layers:
            layer["x1"] -= layer["speed"]
            layer["x2"] -= layer["speed"]

            # Reinicia a posição das camadas para loop contínuo
            if layer["x1"] <= -layer["width"]:
                layer["x1"] = layer["x2"] + layer["width"]
            if layer["x2"] <= -layer["width"]:
                layer["x2"] = layer["x1"] + layer["width"]

    def draw(self):
        # Desenha as camadas do fundo de forma que cubram toda a altura e largura da tela
        for layer in self.layers:
            # Desenha a primeira camada
            self.window.blit(layer["image"], (layer["x1"], 0))
            # Desenha a segunda camada
            self.window.blit(layer["image"], (layer["x2"], 0))
