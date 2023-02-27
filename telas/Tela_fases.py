import pygame 
from multiuso import *
from fases.Fase import criar_fase

class Tela_fases():

    def __init__(self):
        self.fundo = pygame.image.load('Assets\\tela_fases\\fases.png').convert_alpha()
        self.rect_botao_fase0 = (260, 170, 280, 50)
        self.rect_botao_fase1 = (260, 260, 280, 50)
        self.rect_botao_fase2 = (260, 350, 280, 50)
        self.rect_botao_fase3 = (260, 440, 280, 50)
        self.rect_botao_fase4 = (260, 530, 280, 50)
    

    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if colisao_ponto_retangulo(self.rect_botao_fase0, event.pos[0],event.pos[1]):
                        return criar_fase(0)
                    elif colisao_ponto_retangulo(self.rect_botao_fase1, event.pos[0],event.pos[1]):
                        return criar_fase(1)
                    elif colisao_ponto_retangulo(self.rect_botao_fase2, event.pos[0],event.pos[1]):
                        return criar_fase(2)
                    elif colisao_ponto_retangulo(self.rect_botao_fase3, event.pos[0],event.pos[1]):
                        return criar_fase(3)
                    elif colisao_ponto_retangulo(self.rect_botao_fase4, event.pos[0],event.pos[1]):
                        return criar_fase(4)
        return self    
                
                
    def desenha(self,screen,font):
        screen.fill(PRETO)
        screen.blit(self.fundo,(0,0))