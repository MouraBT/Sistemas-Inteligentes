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
        #O custo é o valor que está na matriz
        def __init__(self,custo,  Node_esquerdo, Node_direito):
            self.custo = custo
            self.filho_esquerdo = Node_esquerdo
            self.filho_direito = Node_direito


    def __init__(self):
        #ver como faz polimorfismo ou a declaração para que raiz seja inicializado ja como Node
        self.raiz = None
        self.lista_visitados = []
        self.tamanho_arvore = 0
    #def insere_node(self):
        #verifica se a arvore existe
        #caso arvore vazia
        #insere esquerda
        #insere direita
    #def deleta_node()
    #def deleta_arvore(self):
    def arvore_vazia(self):
        if(self.raiz == None):
            return True
        else:
            return False
    def ler_node_esquerdo(self,node_atual):
        return node_atual.filho_esquerdo
    def ler_node_direito(self,node_atual):
        return node_atual.filho_direito

    def procura_na_lista(self,node):
        for i in range(0,len(self.lista_visitados)):
            if(i == self.lista_visitados[i]):
                return True
        return False

    def guarda_node(self, node):
        if(self.procura_na_lista(self,node) == False):
            self.lista_visitados.append(node)
            return True
        else:
            return False
#O agente irá herda a árvore e ela será utilizado no metodo de busca dentro do agente
#Classe agente

class Agente:

    # Construtor
    def __init__(self, labirinto):
        #Valor que representa o agente
        self.valor_agente = 2
        #Valor que representa o objetivo
        self.valor_objetivo = 3

        #Posição atual do Agente  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_atual_x = 0
        self.posicao_atual_y = 0

        #Labirinto que o agente terá que percorrer
        self.labirinto = labirinto

        #Posição inicial do Agente  na  matriz labirinto, onde x = linha e y = coluna
        self.localiza_agente()
        self.posicao_inicial_x = self.posicao_atual_x
        self.posicao_inicial_y = self.posicao_atual_y

        # Posição do objetivo  na  matriz labirinto, onde x = linha e y = coluna
        self.localiza_objetivo()

        #Cria uma matriz para colocar o valor dos custos
        self.matriz_de_custos = []
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(0)
            self.matriz_de_custos.append(linha)

    #Função que localiza a posição atual do agente
    def localiza_agente(self):
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 2:
                    self.posicao_atual_x = i
                    self.posicao_atual_y = j

    # Função que localiza a posição atual do agente
    def localiza_objetivo(self):
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 3:
                        self.posicao_objetivo_x = i
                        self.posicao_objetivo_y = j

    #Funções para movimentar o agente
    def andar_para_direita(self):
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
        self.posicao_atual_y = self.posicao_atual_y + 1
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

    def andar_para_esquerda(self):
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
        self.posicao_atual_y = self.posicao_atual_y - 1
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

    def andar_para_cima(self):
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
        self.posicao_atual_x = self.posicao_atual_y - 1
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

    def andar_para_baixo(self):
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
        self.posicao_atual_x = self.posicao_atual_y + 1
        self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

    #Funções para verificar se os espaços estão livres ou não paredes
    def verifica_direita(self):
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 1:
            return True
        else:
            return False

    def verifica_esquerda(self):
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 1:
            return True
        else:
            return False

    def verifica_em_cima(self):
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y - 1] == 1:
            return True
        else:
            return False
    def verifica_em_baixo(self):
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y - 1] == 1:
            return True
        else:
            return False
#Nessa função ele utiliza as funções de verificação. Primeiro ele verifica a direita se o caminho estiver livre ele verifica a matriz de custos
#e atribui o variável maior e decisao = 1. Se esquerda estiver livre e o valor da matriz de custos for maior que a variável  maior
#ele atualiza menor e muda a decisão. a função repete o mesmo procedimento para cima e para baixo.
#O valor da decisao final, a quem tem o menor valor de custo será o quadrado que o agente irá se movimentar.
#O movimento será feito pela chamada da função movimento
#decisao = 1 move para direita
# decisao = 2 move para esquerda
# decisao = 3 move para emcima
# decisao = 4 move para baixo
    def resultado(self):
        menor = 0
        decisao = 0
        if self.verifica_direita() == True:
            menor =  self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y + 1]
            decisao = 1

        if self.verifica_esquerda() == True:
            if self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y] < menor:
                menor = self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y - 1]
                decisao = 2

        if self.verifica_em_cima() == True:
            if self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y] < menor:
                menor = self.matriz_de_custos[self.posicao_atual_x - 1][self.posicao_atual_y]
                decisao = 3

        if self.verifica_em_baixo() == True:
            if self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y] < menor:
                menor = self.matriz_de_custos[self.posicao_atual_x + 1][self.posicao_atual_y]
                decisao = 4

        self.movimenta(self,decisao)

    def movimenta(self, decisao):
        if decisao == 1:
            self.andar_para_direita()
        if decisao == 2:
            self.andar_para_esquerda()
        if decisao == 3:
            self.andar_para_cima()
        if decisao == 4:
            self.andar_para_baixo()

    def objetivo(self):
        if self.posicao_atual_x == self.posicao_objetivo_x and self.posicao_atual_y == self.posicao_objetivo_y:
            return True
        else:
            return False

#    def busca_A(self):



#função que calcula o valor euristico de cada nó
    def calcula_heuristica(self,x,y):
        distancia_x = x - self.posicao_objetivo_x
        distancia_y = y - self.posicao_objetivo_y
        distancia_heuristica = distancia_x + distancia_y
        return distancia_heuristica

#Soma o custo heuristico com o calculo uniforme
    #OBS: ESSE CALCULO UNIFORME ESTA ERRADO. TEM QUE VER SE DÁ PARA CALCULAR FORA DA BUSCA
    def calcula_custo_total(self):
        custo_uniforme = 0
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 1:
                    custo_heuristico = self.calcula_heuristica(self, i, j)
                    custo_uniforme = custo_uniforme + 1
                    self.matriz_de_custos[i][j] =  custo_heuristico + custo_uniforme
