import numpy as np
from multiuso import *

class Estrela:

    def __init__(self, pos, dimensao):
        self.pos = pos
        self.raio = dimensao
        self.coletada = False
        
    
    def desenha(self, screen, imagem):
        
        # ajusta a posição da imagem para se encaixar com a posição desejada
        pos = self.pos - np.array([self.raio*1.75, self.raio*1.75])

        screen.blit(imagem, pos)
    
    # verifica colisão entre bola e estrela
    def colisao_bola(self, pos_bola):

        distancia = distancia_entre_pontos(self.pos, pos_bola)
        if distancia <= self.raio + 8:
            return True
        return False
