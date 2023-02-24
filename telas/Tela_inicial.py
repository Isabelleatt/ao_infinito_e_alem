import pygame
import numpy as np
from multiuso import *
from fases.Fase import *
from info_fases import info_fases

class Tela_inicial():
    def __init__(self):
        self.fundo = pygame.image.load('Assets\\tela_inicial\menu_inicial.png').convert_alpha()
        self.rect_botao_play = (360,370,230,40)
        self.rect_botao_regras = (685,450,240,56)
    
    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.rect_botao_play, event.pos[0],event.pos[1]):  
                        i = 0
                        tela = Fase(
                            planetas = info_fases[i]['planetas'],
                            pos_inicial = info_fases[i]['pos_inicial'],
                            bolas = info_fases[i]['bolas'],
                            qtd_bolas = info_fases[i]['qtd_bolas'],
                            estrelas = info_fases[i]['estrelas'],
                            portal = info_fases[i]['portal'],
                            nivel = info_fases[i]['nivel'],
                        )

                        reiniciar_fase(tela)
                        return tela
                    elif colisao_ponto_retangulo(self.rect_botao_regras, event.pos[0],event.pos[1]):
                        return Regras()
        return self    
                
    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.fundo,(0,0))