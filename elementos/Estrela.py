import pygame
import numpy as np
from multiuso import *

class Estrela:

    def __init__(self, pos, dimensao):
        self.pos = pos
        self.raio = dimensao
        self.coletada = False
        
    
    def desenha(self, screen, imagem):
        
        pos = self.pos - np.array([self.raio*1.75, self.raio*1.75])
        # pygame.draw.circle(screen, ROSA, self.pos, self.raio)
        screen.blit(imagem, pos)
    
    def colisao_bola(self, pos_bola):
        # return colisao_ponto_retangulo((self.pos[0], self.pos[0], 35,35), pos_bola[0], pos_bola[1])
        distancia = distancia_entre_pontos(self.pos, pos_bola)
        
        if distancia <= self.raio + 8:
            return True
        return False


        