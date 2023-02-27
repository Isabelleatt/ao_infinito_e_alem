import pygame
from multiuso import *
from fases.Fase import *
from telas.Tela_regras import Regras

class Tela_menu():

    def __init__(self, nivel_atual):
        self.fundo = pygame.image.load('Assets\\tela_inicial\menu_inicial.png').convert_alpha()
        self.rect_botao_play = (360,370,230,40)
        self.rect_botao_regras = (360,480,230,40)
        self.nivel_atual = nivel_atual    


    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.rect_botao_play, event.pos[0],event.pos[1]):
                        tela = criar_fase(self.nivel_atual)
                        return tela
                    
                    elif colisao_ponto_retangulo(self.rect_botao_regras, event.pos[0],event.pos[1]):
                        return Regras()
        return self    
                

    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.fundo,(0,0))