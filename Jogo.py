import pygame
from random import *
from math import *
from fases.Fase_1 import Fase_1
# from fases.Fase_2 import Fase_2

#VARIAVEIS
# WIDTH = 1000
# HEIGHT = 5500

WIDTH = 800
HEIGHT = 700

#CORES

class Jogo:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Ao infinito e além!")
        self.tela_atual = Fase_1()
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.fonte = pygame.font.SysFont('Anton', 30)
    
    def atualiza(self):

        self.tela_atual = self.tela_atual.atualiza()
        self.clock.tick(self.fps)

        if self.tela_atual is None:
            return False
        return True

    def game_loop(self):
        while self.atualiza():
            self.tela_atual.desenha(self.screen, self.fonte)
            pygame.display.update()
    
    def finaliza(self):
        pygame.quit()