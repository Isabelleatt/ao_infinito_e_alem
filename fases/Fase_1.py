import pygame
import numpy as np
from elementos.Planeta import Planeta
from elementos.Bola import Bola
from elementos.Estrela import Estrela
from multiuso import *



class Fase_1():
    def __init__(self) :

        # planetas
        self.planetas = [Planeta(np.array([500,400]), 35, 500)]

        # bolas
        self.pos_inicial = np.array([350,250])
        self.bolas = [Bola(self.pos_inicial, np.array([7,7])) for _ in range(3)]
        self.indice = 0
        self.atual = self.bolas[0] # bola que está sendo lançada

        # lançamento
        self.pos_final = np.array([0,0])
        self.tentativa = False # indica se a bola já está em andamento (true) ou não (false)

        # estrelas
        self.estrelas = [Estrela(np.array([550, 450]), 7), Estrela(np.array([515, 465]), 7), Estrela(np.array([470, 470]), 7)]
        self.pontos = 0 # qtd de estrelas coletadas


    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     self.pos_inicial = np.array([250,250])
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self.pos_final = pygame.mouse.get_pos()
                self.atual.lancada = 1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.atual.vel = np.array([0,0])

                    self.atual.surface.fill(CINZA)
                    self.indice += 1
                    self.atual = self.bolas[self.indice]
                    self.tentativa = False
                    return self
    
        # if self.indice > 2:
        #     return 
        self.tentativa = self.atual.lancamento(self.tentativa, self.pos_inicial, self.pos_final)
        
        if self.tentativa:
            for planeta in self.planetas:
                self.atual.a, self.atual.vel = planeta.calcula_gravidade(self.atual.pos, 10000, self.atual.a, self.atual.vel)
                if planeta.colisao_bola(self.atual.pos):
                    self.atual.vel = 0
        
        # verifica se a bola saiu da tela
        if self.atual.saiu_tela(WIDTH, HEIGHT):
            self.indice += 1
            self.atual.surface.fill(CINZA)
            self.atual = self.bolas[self.indice]
            self.atual.surface.fill(VERDE)
            self.tentativa = False
            return self
        
        # verifica se a bola colidiu com algum planeta

        # movimenta a bola
        self.atual.movimento()

        # verifica a colisão da bola com cada uma estrelas
        for estrela in self.estrelas:

            if estrela.colisao_bola(self.atual.pos) and not estrela.coletada:
                self.pontos += 1
                estrela.coletada = True
    
        return self


    def desenha(self, screen, fonte):
        screen.fill((0,0,0))
        for planeta in self.planetas:
            planeta.desenha(screen, ROSA)

        for i in range(self.indice+1):
            bola = self.bolas[i]
            if i == self.indice:
                bola.desenha(screen, VERDE)
            else:
                bola.desenha(screen, CINZA)

        for estrela in self.estrelas:
            if not estrela.coletada:
                estrela.desenha(screen, AMARELO)
        
        if self.atual.lancada == 0:
            pygame.draw.line(screen, BRANCO, self.pos_inicial, pygame.mouse.get_pos(), 2)
        if self.indice >=1:
            pygame.draw.line(screen, CINZA, self.pos_inicial, self.pos_final, 1)
        
        estrela = Estrela(np.array([WIDTH-60, 20]), 6).desenha(screen, AMARELO)
        vidas = [Bola(np.array([20 + i*20,20]), np.array([8,8])) for i in range(3-self.indice)]
        for i in vidas:
            i.desenha(screen, VERDE)

        pontos = fonte.render(f'{self.pontos:.0f}', False, BRANCO)
        screen.blit(pontos, (WIDTH-40,10))