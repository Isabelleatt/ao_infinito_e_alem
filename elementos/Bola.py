import pygame
import numpy as np

def limita_velocidade(v):
        if abs(v) > 50: 
            if v > 0:
                return 50
            return -50
        return v

class Bola():

    def __init__(self, posicao, dimensao):
        self.pos = posicao # [x, y]
        self.dim = dimensao # [h, w]
        self.vel = np.array([0,0])
        self.surface = pygame.Surface(dimensao)
        self.pos_centro = self.pos + np.array([self.dim[0]/2, self.dim[1]/2])
        
        self.lancada = 0 # 0 - ainda não foi lançada, 1 - acabou de ser lançada, 2 - já está em movimento
        self.a = np.array([1,1]) # aceleração


    def desenha(self, screen, cor):
        rect = pygame.Rect(self.pos, self.dim)
        self.surface.fill(cor)
        screen.blit(self.surface, rect)
    

    def lancamento(self, tentativa, pos_mouse):
        if self.lancada == 1 and not tentativa:
            self.lancada = 2
            tentativa = True

            direcao = np.array(self.pos_centro) - np.array(pos_mouse)

            modulo_vetor = np.linalg.norm(direcao)
            vetor_aceleracao = direcao/ modulo_vetor

            mag_a = abs(direcao)

            self.vel = vetor_aceleracao * mag_a
            
            self.vel[0] = limita_velocidade(self.vel[0])
            self.vel[1] = limita_velocidade(self.vel[1])
            
        if self.lancada == 0:
            return False
        return True
    

    # verifica se a bolinha saiu da tela
    def saiu_tela(self, w, h):
        if self.pos[0] < 10  or self.pos[0] > w - 10 or self.pos[1] < 10 or self.pos[1] > h - 10:
            return True
        return False


    # calcula o movimento da bolinha
    def movimento(self):
        self.pos = self.pos + 0.1 * self.vel
    
    
    # reinicia os atributos do objeto
    def reiniciar(self):
        self.vel = np.array([0,0])
        self.surface = pygame.Surface(self.dim)
        self.lancada = 0
