from multiuso import * 

class Soprador():
    def __init__(self, posicao, dimensao, alcance, direcao):
        self.pos = posicao
        self.dim = dimensao
        self.alc = alcance
        self.assoprou = False
        self.direcao = direcao
    
    def desenha(self, screen, imagem):
        screen.blit(imagem, self.pos)

    def assoprar(self, vel_bola, a_bola):
        
        if self.direcao == 'direita':
            vel_bola = np.array([abs(vel_bola[0]), vel_bola[1]*0.3])
            a = a_bola * np.array([300,0])

        elif self.direcao == 'esquerda':
            vel_bola = np.array([abs(vel_bola[0]) * -1, vel_bola[1]*0.3])
            a = a_bola * np.array([-300,0])

        elif self.direcao == 'cima':
            vel_bola = np.array([vel_bola[0]*0.3, abs(vel_bola[1])])
            a = a_bola * np.array([0,300])

        elif self.direcao == 'baixo':
            vel_bola = np.array([vel_bola[0]*0.3, abs(vel_bola[1]) * -1])
            a = a_bola * np.array([0,-300])

        vel_bola = vel_bola + a
        return vel_bola
