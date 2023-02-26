import pygame
from multiuso import *
from telas.Tela_menu import Tela_menu

class Tela_final():
    def __init__(self, fase_atual):
        self.fundo = pygame.image.load('Assets\\resultado\ganhou_final.png').convert_alpha()
        self.rect_botao_menu = (425,309,280,40)
        self.rect_botao_again = (425,404,280,60)
        self.fase_atual = fase_atual
        self.nivel = fase_atual.nivel
    
    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.rect_botao_menu, event.pos[0],event.pos[1]):
                        return Tela_menu(self.nivel)
                    elif colisao_ponto_retangulo(self.rect_botao_again, event.pos[0],event.pos[1]):  
                        tela = self.fase_atual
                        return tela

        return self    
                
    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.fundo,(0,0))