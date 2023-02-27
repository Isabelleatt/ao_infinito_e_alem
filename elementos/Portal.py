import pygame
import numpy as np
from multiuso import *

class Portal():
    def __init__(self, posicao1, posicao2, dimensao1, dimensao2) :
        # cada objeto consiste no par de portal
        self.pos1 = posicao1 # posição do portal 1
        self.pos2 = posicao2 # posição do portal 2
        self.dim1 = dimensao1
        self.dim2 = dimensao2
        self.surface1 = pygame.Surface(dimensao1)
        self.surface2 = pygame.Surface(dimensao2)
    
    def desenha(self, screen, cor):
        rect1 = pygame.Rect(self.pos1, self.dim1)
        self.surface1.fill(cor)
        screen.blit(self.surface1, rect1)

        rect2 = pygame.Rect(self.pos2, self.dim2)
        self.surface2.fill(cor)
        screen.blit(self.surface2, rect2)
    

    def teletransporta(self, vel_bola, pos_bola):

        if colisao_ponto_retangulo((self.pos1[0],self.pos1[1], self.dim1[0], self.dim1[1]), pos_bola[0], pos_bola[1]):
            pos_bola = self.pos2 

        elif colisao_ponto_retangulo((self.pos2[0],self.pos2[1], self.dim2[0], self.dim2[1]), pos_bola[0], pos_bola[1]):
            pos_bola = self.pos1

        return vel_bola, pos_bola
        
