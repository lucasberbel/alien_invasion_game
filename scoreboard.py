import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """Uma classe para informar a pontuação"""

    def __init__(self, ai_settings, screen, stats):
        """"Inicia os atributos de manutenção da pontuação"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #configurações de fonte para informar pontuação
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)

        #preparar as imagens de pontuação inicial
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Transformar a pontuação em uma imagem"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        #executa a pontuação a na parte de cima a direita da tela
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect_top = 20

    def show_score(self):
        """Desenha a pontuação na tela"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        #desenhar espaçonaves
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Transformar a pontuação mais alta em um imagem"""
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color, self.ai_settings.bg_color)

        #centralizar a pontuação mais alta no alto da tela
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Transforma a fase do jogo em uma imagem"""
        self.level_image = self.font.render(str(self.stats.level), True,
                                            self.text_color, self.ai_settings.bg_color)

        #posiciona a fase do jogo abaixo da pontuação
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
