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
    def
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
#A classe arvore conterá os nós e será criado a partir do nó raiz que é o estado inicial do agente. Ela será usado na busca
#realizada pelo agente que encontrará o melhor caminho.
#Classe arvore
class Arvore:
    class Node:
        def __init__(self, distancia_saida,custo_uniforme, Node_esquerdo, Node_direito):
            self.valor = valor
            self.filho_esquerdo = Node_esquerdo
            self.filho_direito = Node_direito

    def __init__(self)
        self.raiz = Node
    def criar_node(self, lado):
    def ler_node_esquerdo(self):
    def ler_node_direito(self):
    def deleta_node(self):
#O agente irá herda a árvore e ela será utilizado no metodo de busca dentro do agente
#Classe agente

class Agente:
    # Construtor
   def __init__(self, x, y):
       self.estado_atual = 2
       self.objetivo = 3
       self.estado_inicial_x = x
       self.estado_inicial_x = y
   def sucessor(self):
   def resultado(self):
   def objetivo(self):
   def busca_A(self):