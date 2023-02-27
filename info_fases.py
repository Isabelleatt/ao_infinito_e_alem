import numpy as np
from elementos.Planeta import Planeta
from elementos.Bola import Bola
from elementos.Estrela import Estrela
from elementos.Portal import Portal
from elementos.Soprador import Soprador

info_fases =[
    {
        "planetas": [Planeta(np.array([-100,-100]), 0.1, 0, 10)],
        "pos_inicial": np.array([250,350]),
        "bolas": [Bola(np.array([250,350]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([550, 250]), 13), Estrela(np.array([550, 350]), 13), Estrela(np.array([550, 450]), 13)],
        "portal": False,
        "soprador": False,
        "nivel": 0
    },
    {
        "planetas": [Planeta(np.array([500,400]), 40, 500, 30000)],
        "pos_inicial": np.array([340,230]),
        "bolas": [Bola(np.array([340,230]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([560, 480]), 13), Estrela(np.array([500, 490]), 13), Estrela(np.array([440, 470]), 13)],
        "portal": False,
        "soprador": False,
        "nivel": 1
    },
    {
        "planetas": [Planeta(np.array([500,400]), 50, 400, 20000), Planeta(np.array([200,200]), 40, 200, 5000),],
        "pos_inicial": np.array([100,100]),
        "bolas": [Bola(np.array([100,100]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([590, 390]), 13), Estrela(np.array([535, 300]), 13), Estrela(np.array([215, 120]), 13)],
        "portal": False,
        "soprador": False,
        "nivel": 2
    },
    {
        "planetas": [Planeta(np.array([300,550]), 50, 450, 10000), Planeta(np.array([550,400]), 40, 450, 10000),],
        "pos_inicial": np.array([120,140]),
        "bolas": [Bola(np.array([120,140]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([630, 590]), 13), Estrela(np.array([550, 540]), 13), Estrela(np.array([425, 455]), 13)],
        "portal": [Portal(np.array([700,590]), np.array([50,100]), np.array([5,80]), np.array([5,80]))],
        "soprador": False,
        "nivel": 3
    },
        {
        "planetas": [Planeta(np.array([500,480]), 50, 450, 20000), Planeta(np.array([500,150]), 40, 500, 10000),],
        "pos_inicial": np.array([570,330]),
        "bolas": [Bola(np.array([570,330]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([410, 550]), 13), Estrela(np.array([400, 480]), 13), Estrela(np.array([405, 190]), 13)],
        "portal": [Portal(np.array([400,620]), np.array([190,100]), np.array([80,5]), np.array([80,5]))],
        "soprador": Soprador(np.array([50,140]), np.array([80,80]), 150, 'direita'),
        "nivel": 4
    },
]