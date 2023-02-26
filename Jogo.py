import pygame
from random import *

from telas.Tela_menu import Tela_menu
from telas.Tela_vitoria import Tela_vitoria
from telas.Tela_derrota import Tela_derrota
from telas.Tela_final import Tela_final
from fases.Fase import *

from info_fases import info_fases
from multiuso import *



#CORES

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ao infinito e além!")
        
        self.nivel_atual = 4
        self.tela_atual = Tela_menu(self.nivel_atual)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.fonte = pygame.font.SysFont('Anton', 50)
        
    
    def atualiza(self):

        self.tela_atual = self.tela_atual.atualiza()
        self.clock.tick(self.fps)

        if self.tela_atual is None:
            return False
        
        elif self.tela_atual == "vitoria":
            fase_atual, proxima_fase = vitoria(self.nivel_atual)
            self.tela_atual = Tela_vitoria(fase_atual, proxima_fase)
        
        elif self.tela_atual == "final":
            fase_atual = derrota(self.nivel_atual)
            self.tela_atual = Tela_final(fase_atual)
        
        elif self.tela_atual == "derrota":
            fase_atual = derrota(self.nivel_atual)
            self.tela_atual = Tela_derrota(fase_atual)


        if type(self.tela_atual) is Fase:
            self.nivel_atual = self.tela_atual.nivel

        return True

    def game_loop(self):
        while self.atualiza():
            self.tela_atual.desenha(self.screen, self.fonte)
            pygame.display.update()
    
    def finaliza(self):
        pygame.quit()