from collections import deque
import numpy as np

class Labirinto:

    #funções da classe
    #Construtor tem que ter o self em todas as chamadas de variável da classe
    def __init__(self):
        # variaveis da classe
        self.matriz_labirinto = []
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(0)
            self.matriz_labirinto.append(linha)

    #imprime matriz
    def imprime_matriz(self):
            print(np.matrix(self.matriz_labirinto))
    #cria um labirinto estático
        self.matriz_labirinto[0][5] = 2
        self.matriz_labirinto[9][5] = 3
        for i in range(1, 9):
          self.matriz_labirinto[i][5] = 1
        #
      #  for i in range(1,4):
      #      self.matriz_labirinto[i][0] = 1
       # for i in range(1,8):
       #     self.matriz_labirinto[3][i] = 1
       # for i in range(4,10):
       #     self.matriz_labirinto[i][7] = 1
       # for i in range(3, 7):
       #     self.matriz_labirinto[i][3] = 1
       # for i in range(3, 7):
       #     self.matriz_labirinto[i][5] = 1
       # for i in range(2, 6):
       #     self.matriz_labirinto[6][i] = 1
       # for i in range(4, 7):
       #     self.matriz_labirinto[9][i] = 1
#Classe arvore


# Classe agente
#class Agente:
    # Construtor
 #   def __init__(self):