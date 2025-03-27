import pygame

class ParallaxBackground:
    def __init__(self, window, image_paths, speeds):
        self.window = window
        self.layers = []

        # Carregar as imagens e configurar as posições iniciais
        for i, path in enumerate(image_paths):
            image = pygame.image.load(path).convert_alpha()  # Carregar imagem com transparência
            width = image.get_width()
            height = image.get_height()
            self.layers.append({
                "image": image,
                "x1": 0,
                "x2": width,  # O segundo x começa logo após o primeiro
                "speed": speeds[i],  # A velocidade do parallax para cada camada
                "width": width,
                "height": height  # Altura da imagem para desenhar corretamente
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
        # Desenha as camadas do fundo
        for layer in self.layers:
            # Desenha as duas camadas (x1 e x2) para dar o efeito de movimento contínuo
            self.window.blit(layer["image"], (layer["x1"], 0))  # Desenha a primeira camada
            self.window.blit(layer["image"], (layer["x2"], 0))  # Desenha a segunda camada
