import pygame
from random import *
from math import *

#VARIAVEIS
WIDTH = 1000
HEIGHT = 5500

#CORES

class Jogo:
    # Desenhar circulo
    def desenha_circulo(self, x, y, raio, cor):

        pygame.draw.circle(self.tela, cor, (x, y), raio)
        self.tela.blit(self.tela, (0, 0))


