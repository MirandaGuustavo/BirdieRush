import pygame

from const import COLOR_WHITE, COLOR_GRAY, COLOR_BLACK, COLOR_YELLOW

class Menu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont('Snap ITC', 48)

        self.title = self.font.render("Birdie Rush", True, COLOR_YELLOW)
        self.start_text = "Press SPACE to Start"
        self.mute_text = "Press M to Mute/Un-mute"

        # definir o som de fundo
        pygame.mixer.init()
        pygame.mixer.music.load('../assets/music.wav')
        pygame.mixer.music.play(-1, 0.0)

        # variável de mute
        self.is_muted = False

        # Criar o fundo
        self.background = pygame.image.load("../assets/background_image.png").convert()  # Imagem de fundo
        self.background = pygame.transform.scale(self.background, (
        window.get_width(), window.get_height()))  # Ajustar ao tamanho da tela

        # inicializar transições e efeitos
        self.alpha = 0
        self.fade_in = True

    def show(self, game):
        clock = pygame.time.Clock()  # controle de FPS
        while True:
            self.window.fill(COLOR_BLACK)

            # exibe o fundo
            self.window.blit(self.background, (0, 0))


            if self.fade_in:
                if self.alpha < 255:
                    self.alpha += 5
                else:
                    self.fade_in = False
            title_with_effect = self.title.copy()
            title_with_effect.set_alpha(self.alpha)

            self.window.blit(title_with_effect, (self.window.get_width() // 2 - self.title.get_width() // 2, 100))
            self._draw_text_with_shadow(self.start_text, 300)
            self._draw_text_with_shadow(self.mute_text, 350)

            pygame.display.flip()

            # eventos de teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()
                        game.run()
                        return
                    elif event.key == pygame.K_m:
                        self.toggle_mute()

            # controle de FPS
            clock.tick(60)

    def _draw_text_with_shadow(self, text, y_position):

        rendered_text = self.font.render(text, True, COLOR_WHITE)

        shadow = self.font.render(text, True, COLOR_GRAY)

        self.window.blit(shadow, (self.window.get_width() // 2 - rendered_text.get_width() // 2 + 2, y_position + 2))
        self.window.blit(rendered_text, (self.window.get_width() // 2 - rendered_text.get_width() // 2, y_position))

    def toggle_mute(self):
        if self.is_muted:
            pygame.mixer.music.set_volume(1.0)
            self.is_muted = False
        else:
            pygame.mixer.music.set_volume(0.0)
            self.is_muted = True
