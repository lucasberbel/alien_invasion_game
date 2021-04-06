import pygame
import sys
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group


def run_game():
    #Inicializa o pygame, as configurações e o objeto screen
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height ))
    pygame.display.set_caption("Alien Invasion")

    #Cria o botão play
    play_button = Button(ai_settings, screen, "Play")

    #Cria uma instancia para armazenar dados estatísticos do jogo e cria uma tabela de pontos
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    #Cria uma espaçonave
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # cria uma frota alienígena
    gf.create_fleet(ai_settings,screen,ship,aliens)

    #Cria um grupo onde serão armazenados os projéteis
    bg_color = (230,230,230)

    #Inicia o laço principal do jogo
    while True:
        #Observa eventos de teclado e de mouse
            gf.check_events(ai_settings,screen,stats,sb, play_button, ship,aliens, bullets)

            if stats.game_active:
                ship.update()
                gf.update_bullets(ai_settings, screen,stats,sb, ship, aliens, bullets)
                gf.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)

            gf.update_screen(ai_settings, screen,stats,sb, ship, aliens, bullets, play_button)

            # Redesenha a tela a cada passagem pelo laço
            screen.fill(ai_settings.bg_color)
            ship.blitme()

            # Deixa a tela mais recente visível
            pygame.display.flip()

run_game()
