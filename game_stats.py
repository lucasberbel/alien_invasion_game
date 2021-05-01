class GameStats():
    """Armazena dados estatísticos da invasão alienígena"""

    def __init__(self, ai_settings):
        """Inicializa dados estatísticos"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Inicia a invasão alienígena em um estado inativo
        self.game_active = False

        #Record de pontos não deve ser reiniciado
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
