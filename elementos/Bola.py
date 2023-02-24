import pygame
import numpy as np

class Bola():

    def __init__(self, posicao, dimensao):
        self.pos = posicao # [x, y]
        self.dim = dimensao # [h, w]
        self.vel = np.array([0,0])
        self.surface = pygame.Surface(dimensao)

        
        self.lancada = 0 # 0 - ainda não foi lançada, 1 - acabou de ser lançada, 2 - já está em movimento
        self.a = np.array([0,0]) # aceleração

    def desenha(self, screen, cor):
        rect = pygame.Rect(self.pos, self.dim)
        self.surface.fill(cor)
        screen.blit(self.surface, rect)

    def lancamento(self, tentativa, pos_inicial, pos_final):
        if self.lancada == 1 and not tentativa:
            self.lancada = 2
            tentativa = True
            direcao = np.array(pos_inicial) - np.array(pos_final)

            modulo_vetor = np.linalg.norm(direcao)
            vetor_aceleracao = direcao/ modulo_vetor

            mag_a = 17

            self.vel = vetor_aceleracao * mag_a
        if self.lancada == 0:
            return False
        return True
    
    def saiu_tela(self, w, h):
        if self.pos[0] < 10  or self.pos[0] > w - 10 or self.pos[1] < 10 or self.pos[1] > h - 10:
            return True
        return False

    def movimento(self):
        self.pos = self.pos + 0.1 * self.vel
