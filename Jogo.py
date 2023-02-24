import pygame
from random import *
import numpy as np
from telas.Tela_inicial import Tela_inicial
from telas.Tela_vitoria import Tela_vitoria
from telas.Tela_derrota import Tela_derrota
from fases.Fase import *

from info_fases import info_fases
from multiuso import *



#CORES

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ao infinito e além!")

        self.tela_atual = Tela_inicial()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.fonte = pygame.font.SysFont('Anton', 30)
        self.nivel_atual = 0
    
    def atualiza(self):

        self.tela_atual = self.tela_atual.atualiza()
        self.clock.tick(self.fps)

        if self.tela_atual is None:
            return False
        
        elif self.tela_atual == "vitoria":
            fase_atual, proxima_fase = vitoria(self.nivel_atual)
            self.tela_atual = Tela_vitoria(fase_atual, proxima_fase)
        
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