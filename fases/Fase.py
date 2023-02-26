import pygame
import numpy as np
from elementos.Planeta import Planeta
from elementos.Bola import Bola
from elementos.Estrela import Estrela
from elementos.Portal import Portal
from multiuso import *
from info_fases import info_fases

# from telas.Tela_vitoria import Tela_vitoria

class Fase():
    def __init__(self, planetas, bolas, pos_inicial, qtd_bolas, estrelas, nivel,portal= False) :

        pygame.mixer.init()

        # planetas
        self.planetas = planetas

        # bolas
        self.pos_inicial = pos_inicial
        self.bolas = bolas
        self.indice = 0
        self.atual = self.bolas[0] # bola que está sendo lançada
        self.n_bolas = qtd_bolas

        # lançamento
        self.pos_final = np.array([0,0])
        self.tentativa = False # indica se a bola já está em andamento (true) ou não (false)

        # estrelas
        self.estrelas = estrelas
        self.pontos = 0 # qtd de estrelas coletadas
        self.nivel = nivel
        self.portais = portal

        self.primeiro_click = True

        self.fundo = pygame.image.load('Assets\\background\\fundo.png').convert_alpha()
        self.vida = pygame.image.load('Assets\\vidas\\gato_vivo.png').convert_alpha()
        self.morto = pygame.image.load('Assets\\vidas\\gato_morto.png').convert_alpha()
        # self.imagem_bola = pygame.transform.scale(self.vida, (40,40))
        self.img_estrela = pygame.image.load('Assets\\recompensa\estrela.png').convert_alpha()
        self.img_planeta_80 = pygame.image.load('Assets\\planetas\planeta_80.png').convert_alpha()
        self.img_planeta_100 = pygame.image.load('Assets\\planetas\planeta_100.png').convert_alpha()
        self.img_pontos = pygame.transform.scale(self.img_estrela, (50,50))

        # Efeitos sonoros
        self.som_coletou = pygame.mixer.Sound('Assets/efeitos_sonoros/bonus.mp3')
        


    def atualiza(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            # elif event.type == pygame.MOUSEBUTTONDOWN:
            #     self.pos_inicial = np.array([250,250])
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if self.primeiro_click:
                    self.primeiro_click = False
                    pygame.time.delay(100)
                else:
                    self.pos_final = pygame.mouse.get_pos()
                    self.atual.lancada = 1

            elif event.type == pygame.KEYDOWN:
                
                # caso o usuário aperte p, ele pode lançar a próxima bola
                if event.key == pygame.K_p:
                    self.indice += 1
                    # DERROTA
                    if self.indice >= self.n_bolas:
                        return "derrota"
                    self.atual = self.bolas[self.indice]
                    self.tentativa = False
                    
                    
                    return self


        # realiza o lançamento da bola
        self.tentativa = self.atual.lancamento(self.tentativa, self.pos_inicial, self.pos_final)
        
        if self.tentativa:
            for planeta in self.planetas:

                # calcula a gravidade atrelada a cada planeta
                self.atual.a, self.atual.vel = planeta.calcula_gravidade(self.atual.pos, self.atual.a, self.atual.vel)
                
                # verifica se a bola colidiu com algum planeta
                if planeta.colisao_bola(self.atual.pos):
                    self.indice += 1
           
                    self.atual = self.bolas[self.indice]
          
                    self.tentativa = False
                    return self
        
        # verifica se a bola saiu da tela
        if self.atual.saiu_tela(WIDTH, HEIGHT):
            self.indice += 1

            # DERROTA
            if self.indice >= self.n_bolas:
                return "derrota"
            
            self.atual = self.bolas[self.indice]
            self.tentativa = False

            return self
        
        # se houver portal, verifica a possibilidade de teletransportar
        if self.portais:
            for portal in self.portais:
                self.atual.vel, self.atual.pos = portal.teletransporta(self.atual.vel, self.atual.pos, True)

        # movimenta a bola
        self.atual.movimento()

        # verifica a colisão da bola com cada uma estrelas
        for estrela in self.estrelas:

            if estrela.colisao_bola(self.atual.pos) and not estrela.coletada:
                pygame.mixer.Sound.play(self.som_coletou)
                self.pontos += 1
                estrela.coletada = True

        # VITÓRIA
        if self.pontos == 3:
            if self.nivel == 4:
                return "final"
            return "vitoria"
        
        
    
        return self


    def desenha(self, screen, fonte):
        screen.fill((0,0,0))
        screen.blit(self.fundo,(0,0))

        # PLANETAS
        for planeta in self.planetas:
            if planeta.raio == 80:
                planeta.desenha(screen, self.img_planeta_80)
            else:
                planeta.desenha(screen, self.img_planeta_100)

        # BOLAS
        for i in range(self.indice+1):
            bola = self.bolas[i]
            if i == self.indice:
                bola.desenha(screen, LARJ)
            else:
                bola.desenha(screen, ROSA)

        # ESTRELAS
        for estrela in self.estrelas:
            if not estrela.coletada:
                estrela.desenha(screen, self.img_estrela)
        
        # LINHA DE LANÇAMENTO
        if self.atual.lancada == 0: # desnha a linha do lançamento atual
            pygame.draw.line(screen, BRANCO, self.atual.pos_centro, pygame.mouse.get_pos(), 2)
        if self.indice >=1: # desenha a linha do último lançamento
            pygame.draw.line(screen, CINZA, self.atual.pos_centro, self.pos_final, 1)
        
        # número de estrelas pegas
        estrela = Estrela(np.array([WIDTH-90, 10]), 6).desenha(screen, self.img_pontos)
        pontos = fonte.render(f'{self.pontos:.0f}', False, BRANCO)
        screen.blit(pontos, (WIDTH-50,10))

        # número de vidas restantes
        n_vidas = self.n_bolas-self.indice
        if self.atual.lancada == 2:
            n_vidas -=1

        # vidas = [Bola(np.array([20 + i*20,20]), np.array([8,8])) for i in range(n_vidas)]
        # pos_vidas = [np.array([20 + i*50,20]) for i in range(n_vidas)]
        for i in range(self.n_bolas):
            pos = np.array([20 + i*50,15])
            if i < n_vidas:
                screen.blit(self.vida, pos)
            else:
                screen.blit(self.morto, pos)
        # for i in pos_vidas:
        #     # i.desenha(screen, VERDE)
            

        # PORTAIS
        cores_portais = [ROXO, AZUL]
        if self.portais:
            for i in range(len(self.portais)):
                portal = self.portais[i]
                portal.desenha(screen, cores_portais[i])
    
# FUNÇÕES DE CRIAÇÃO DE FASE #############################################################
def derrota(nivel_atual):
    i = nivel_atual
    fase_atual = Fase(
                planetas = info_fases[i]['planetas'],
                pos_inicial = info_fases[i]['pos_inicial'],
                bolas = info_fases[i]['bolas'],
                qtd_bolas = info_fases[i]['qtd_bolas'],
                estrelas = info_fases[i]['estrelas'],
                portal = info_fases[i]['portal'],
                nivel = info_fases[i]['nivel'],
            )
    reiniciar_fase(fase_atual)
    return fase_atual

def vitoria(nivel_atual):
    i = nivel_atual
    fase_atual = Fase(
                planetas = info_fases[i]['planetas'],
                pos_inicial = info_fases[i]['pos_inicial'],
                bolas = info_fases[i]['bolas'],
                qtd_bolas = info_fases[i]['qtd_bolas'],
                estrelas = info_fases[i]['estrelas'],
                portal = info_fases[i]['portal'],
                nivel = info_fases[i]['nivel'],
            )
    reiniciar_fase(fase_atual)
    i += 1
    proxima_fase = Fase(
                        planetas = info_fases[i]['planetas'],
                        pos_inicial = info_fases[i]['pos_inicial'],
                        bolas = info_fases[i]['bolas'],
                        qtd_bolas = info_fases[i]['qtd_bolas'],
                        estrelas = info_fases[i]['estrelas'],
                        portal = info_fases[i]['portal'],
                        nivel = info_fases[i]['nivel'],
                    )
    return fase_atual, proxima_fase

def reiniciar_fase(fase):
    fase.indice = 0
    fase.atual = fase.bolas[0]
    fase.tentativa = False
    fase.pontos = 0
    fase.primeiro_click = True
    for estrela in fase.estrelas:
        estrela.coletada = False
    
    for bola in fase.bolas:
        bola.pos = fase.pos_inicial
        bola.reiniciar()
