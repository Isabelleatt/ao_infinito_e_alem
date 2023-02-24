import numpy as np
from elementos.Planeta import Planeta
from elementos.Bola import Bola
from elementos.Estrela import Estrela
from elementos.Portal import Portal
info_fases =[
    {
        "planetas": [Planeta(np.array([0,0]), 0.1, 0, 10)],
        "pos_inicial": np.array([150,350]),
        "bolas": [Bola(np.array([150,350]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([550, 250]), 13), Estrela(np.array([550, 350]), 13), Estrela(np.array([470, 470]), 13)],
        "portal": False,
        "nivel": 0
    },
    {
        "planetas": [Planeta(np.array([500,400]), 40, 500, 50000)],
        "pos_inicial": np.array([340,230]),
        "bolas": [Bola(np.array([340,230]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([560, 480]), 13), Estrela(np.array([500, 490]), 13), Estrela(np.array([440, 470]), 13)],
        "portal": False,
        "nivel": 1
    },
    {
        "planetas": [Planeta(np.array([500,400]), 50, 400, 20000), Planeta(np.array([200,200]), 40, 200, 5000),],
        "pos_inicial": np.array([100,100]),
        "bolas": [Bola(np.array([100,100]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([590, 390]), 13), Estrela(np.array([535, 300]), 13), Estrela(np.array([215, 120]), 13)],
        "portal": False,
        "nivel": 2
    },
    {
        "planetas": [Planeta(np.array([300,550]), 50, 450, 10000), Planeta(np.array([550,400]), 40, 450, 10000),],
        "pos_inicial": np.array([120,140]),
        "bolas": [Bola(np.array([120,140]), np.array([11,11])) for _ in range(5)],
        "qtd_bolas": 5,
        "estrelas": [Estrela(np.array([630, 590]), 13), Estrela(np.array([550, 540]), 13), Estrela(np.array([425, 455]), 13)],
        "portal": [Portal(np.array([700,590]), np.array([50,100]), np.array([5,60]))],
        "nivel": 3
    },
        {
        "planetas": [Planeta(np.array([450,390]), 50, 450, 20000), Planeta(np.array([200,280]), 40, 500, 10000),],
        "pos_inicial": np.array([520,240]),
        "bolas": [Bola(np.array([520,240]), np.array([11,11])) for _ in range(10)],
        "qtd_bolas": 10,
        "estrelas": [Estrela(np.array([350, 320]), 13), Estrela(np.array([270, 390]), 13), Estrela(np.array([305, 190]), 13)],
        "portal": [Portal(np.array([80,530]), np.array([390,100]), np.array([80,5])), ],
        "nivel": 4
    },
]