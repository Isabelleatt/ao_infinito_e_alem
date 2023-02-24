import pygame
import numpy as np
from multiuso import *

class Portal():
    def __init__(self, posicao1, posicao2, dimensao) :
        # cada objeto consiste no par de portal
        self.pos1 = posicao1 # posição do portal 1
        self.pos2 = posicao2 # posição do portal 2
        self.dim = dimensao
        self.surface1 = pygame.Surface(dimensao)
        self.surface2 = pygame.Surface(dimensao)
    
    def desenha(self, screen, cor):
        rect1 = pygame.Rect(self.pos1, self.dim)
        self.surface1.fill(cor)
        screen.blit(self.surface1, rect1)

        rect2 = pygame.Rect(self.pos2, self.dim)
        self.surface2.fill(cor)
        screen.blit(self.surface2, rect2)
    

    def teletransporta(self, vel_bola, pos_bola, horizontal):
        colisao = False
        if colisao_ponto_retangulo((self.pos1[0],self.pos1[1], self.dim[0], self.dim[1]), pos_bola[0], pos_bola[1]):
            pos_bola = self.pos2
            colisao = True
        elif colisao_ponto_retangulo((self.pos2[0],self.pos2[1], self.dim[0], self.dim[1]), pos_bola[0], pos_bola[1]):
            pos_bola = self.pos1
            colisao = True
        # if colisao:
        #     if horizontal:
        #         return vel_bola, pos_bola
        #     return np.array([vel_bola[0], vel_bola[1] * -1]), pos_bola
        return vel_bola, pos_bola
        
