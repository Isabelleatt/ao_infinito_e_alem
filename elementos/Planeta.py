import pygame
import numpy as np

from multiuso import *

class Planeta():
    def __init__(self, pos, dimensao, atmosfera):
        self.pos = pos # [pos horizontal, pos vertical]
        self.raio = dimensao 
        self.atmosfera = atmosfera
    
    def desenha(self, screen, cor):
        pygame.draw.circle(screen, cor, self.pos, self.raio)
    
    def calcula_gravidade(self,pos_bola, C, a_bola, vel_bola):
        dist = distancia_entre_pontos(self.pos, pos_bola)
        if dist < self.atmosfera:
            # direcionamento em relação a posição atual da bola na direção do planeta
            direcao = self.pos - pos_bola

            # calculo do vetor com a mesma direção do vetor da direção, porém com módulo 1
            modulo_vetor = np.linalg.norm(direcao)
            vetor_aceleracao = direcao/ modulo_vetor

            # cálculo da força gravitacional
            # sendo C o produto entre a constante gravitacional e as massas do planeta e da bola
            mag_a = C / modulo_vetor ** 2

            a_bola = vetor_aceleracao * mag_a
            vel_bola = vel_bola + a_bola

        return a_bola, vel_bola
    
    def colisao_bola(self, pos_bola):
        distancia = distancia_entre_pontos(self.pos, pos_bola)
        if distancia <= self.raio + 5:
            return True
        return False