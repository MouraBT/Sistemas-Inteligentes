#importa a biblioteca para usar fila
from collections import deque

#Classe labirinto
class labirinto:

    #funções da classe
    #Construtor
    def __init__(self):
        # variaveis da classe
        matriz_labirinto = []
    def constroi_matriz():
        matriz=[]
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(0)
        matriz.append(linha)
        return matriz
    #imprime matriz
    def imprime_matriz(matriz):
        for i in range (10):
            for j in range(10):
                print(matriz[i][j])
    def preenche_matriz():
        matriz_labirinto = constroi_matriz()
        matriz_labirinto[0][0] = 2
        matriz_labirinto[10][3] = 3
        for i in range(1,4):
            matriz_labirinto[i][0] = 1
        for i in range(1,8):
            matriz_labirinto[3][i] = 1
        for i in range(4,10):
            matriz_labirinto[i][7] = 1
        for i in range(3, 7):
            matriz_labirinto[i][3] = 1
        for i in range(3, 7):
            matriz_labirinto[i][5] = 1
        for i in range(2, 6):
            matriz_labirinto[6][i] = 1
#Classe arvore

#Classe agente