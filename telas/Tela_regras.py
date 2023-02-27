import pygame
from multiuso import *

class Regras():

    def __init__(self):
        self.tela_regra = 0
        self.lista_regras = [pygame.image.load('Assets/regras/regras_1.png').convert_alpha(),pygame.image.load('Assets/regras/regras_2.png').convert_alpha(),pygame.image.load('Assets/regras/regras_3.png').convert_alpha()]
        self.botao_prox_tela = (700,600,60,60) 
        self.botao_volta_tela = (620,600,60,60)
    

    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.botao_prox_tela, event.pos[0],event.pos[1]):
                        self.tela_regra += 1
                        if self.tela_regra == len(self.lista_regras):                     
                            return "menu"
                    elif colisao_ponto_retangulo(self.botao_volta_tela, event.pos[0],event.pos[1]):
                        self.tela_regra -= 1
                        if self.tela_regra < 0:
                            return "menu"
        return self     
                
                
    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.lista_regras[self.tela_regra],(0,0))