import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont('Arial', 36)
        self.title = self.font.render("Birdie Rush", True, (0, 0, 0))
        self.start_text = self.font.render("Press SPACE to Start", True, (0, 0, 0))
        self.mute_text = self.font.render("Press M to Mute/Unmute", True, (0, 0, 0))

        # Inicializa o mixer do pygame
        pygame.mixer.init()
        pygame.mixer.music.load('../assets/music.wav')
        pygame.mixer.music.play(-1, 0.0)

        self.is_muted = False

    def show(self, game):
        while True:
            self.window.fill((255, 255, 255))  # Limpa a tela
            self.window.blit(self.title, (self.window.get_width() // 2 - self.title.get_width() // 2, 100))
            self.window.blit(self.start_text, (self.window.get_width() // 2 - self.start_text.get_width() // 2, 300))
            self.window.blit(self.mute_text, (self.window.get_width() // 2 - self.mute_text.get_width() // 2, 350))

            pygame.display.flip()

            # Verificar eventos do teclado
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.stop()  # Para a música do menu
                        game.run()
                        return
                    elif event.key == pygame.K_m:
                        self.toggle_mute()

    def toggle_mute(self):

        if self.is_muted:
            pygame.mixer.music.set_volume(1.0)
            self.is_muted = False
        else:
            pygame.mixer.music.set_volume(0.0)
            self.is_muted = True
