import numpy as np 
WIDTH = 800
HEIGHT = 700

# cores ########################
AMARELO = (204, 204, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
CINZA = (80, 80, 80)
PRETO = (0, 0, 0)
ROSA = (255, 0, 127)
ROXO = (148, 0, 211)
VERDE = (30, 200, 20)


# funções #######################
def distancia_entre_pontos(v1, v2):
    return np.sqrt((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2)

def colisao_ponto_retangulo(rect, ponto_x, ponto_y):
        dist_x = ponto_x - rect[0]
        dist_y = ponto_y - rect[1]
        if  0 <= dist_x  <= rect[2] and 0<= dist_y <= rect[3]:
            return True
        else:
            return False
# # 
# class Botão:
#     def __init__(self,coord_x, coord_y, w, h, num ):
#         self.x = coord_x
#         self.y = coord_y
#         self.w = w
#         self.h = h

    