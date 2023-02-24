import pygame
import numpy as np
from multiuso import *
from telas.Tela_inicial import Tela_inicial
from info_fases import info_fases

class Tela_vitoria():
    def __init__(self, fase_atual, prox_fase):
        self.fundo = pygame.image.load('Assets\\resultado\ganhou.png').convert_alpha()
        self.rect_botao_menu = (425,258,230,40)
        self.rect_botao_again = (425,351,240,60)
        self.rect_botao_prox = (425,460,240,60)
        self.fase_atual = fase_atual
        self.nivel = fase_atual.nivel
        self.prox_fase = prox_fase
    
    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.rect_botao_menu, event.pos[0],event.pos[1]):
                        return Tela_inicial()
                    elif colisao_ponto_retangulo(self.rect_botao_again, event.pos[0],event.pos[1]):  
                        tela = self.fase_atual
                        return tela
                    elif colisao_ponto_retangulo(self.rect_botao_prox, event.pos[0],event.pos[1]):  
                        tela = self.prox_fase
                        return tela
        return self    
                
    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.fundo,(0,0))