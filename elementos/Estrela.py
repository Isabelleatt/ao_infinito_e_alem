import pygame
import numpy as np
from multiuso import *

class Estrela:

    def __init__(self, pos, dimensao):
        self.pos = pos
        self.raio = dimensao
        self.coletada = False
    
    def desenha(self, screen, cor):
        pygame.draw.circle(screen, cor, self.pos, self.raio)
    
    def colisao_bola(self, pos_bola):
        distancia = distancia_entre_pontos(self.pos, pos_bola)
        if distancia <= self.raio + 5:
            return True
        return False


        