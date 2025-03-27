import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.game = None  # Inicializa sem o jogo

    def show(self, game):
        """Exibe o menu principal com opções de iniciar e sair."""
        self.game = game  # Agora o menu tem acesso ao jogo
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # Quando o jogador apertar Enter, começa o jogo
                        if self.game:
                            self.game.run()
                            running = False  # Fecha o menu
                    elif event.key == pygame.K_ESCAPE:
                        running = False  # Sair do menu

            # Renderização do menu (opcional)
            self.window.fill((0, 0, 0))  # Cor de fundo
            font = pygame.font.SysFont('Arial', 36)
            text = font.render("Pressione Enter para Iniciar", True, (255, 255, 255))
            self.window.blit(text, (200, 200))  # Posiciona o texto na tela

            pygame.display.update()
