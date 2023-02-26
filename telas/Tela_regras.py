import pygame
from multiuso import *
from fases.Fase import *
from info_fases import info_fases
from telas.Tela_menu import * 

class Regras():

    def __init__(self):
        self.tela_regra = 0
        self.lista_regras = [pygame.image.load('Assets/regras_1/como_jogar.png').convert_alpha(),pygame.image.load('Assets/regras/regras_2.png').convert_alpha(),pygame.image.load('Assets/regras/regras_3.png').convert_alpha()]
        self.botao_prox_tela = (0,0,0,0) 
        self.botao_volta_tela = (0,0,0,0)
    
    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(event.pos[0],event.pos[1], self.botao_prox_tela):
                        self.tela_regra += 1
                        if self.tela_regra == len(self.lista_regras):
                            return Tela_menu()
                    elif colisao_ponto_retangulo(event.pos[0],event.pos[1], self.botao_volta_tela):
                        self.tela_regra -= 1
                        if self.tela_regra < 0:
                            return Tela_menu()
        return self    
                
    def desenha(self,surface):
        surface.fill(BRANCO)
        surface.blit(self.lista_regras[self.tela_regra],(0,0))