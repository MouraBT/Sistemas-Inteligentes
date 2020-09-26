import queuelib as fila
import numpy as np


def cria_labirinto():
    # variaveis da classe
    matriz_labirinto = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        matriz_labirinto.append(linha)
    matriz_labirinto[0][0] = 2
    matriz_labirinto[9][4] = 3
    for i in range(1, 4):
        matriz_labirinto[i][0] = 1
    for i in range(1, 8):
        matriz_labirinto[3][i] = 1
    for i in range(4, 10):
        matriz_labirinto[i][7] = 1
    for i in range(3, 7):
        matriz_labirinto[i][3] = 1
    for i in range(3, 7):
        matriz_labirinto[i][5] = 1
    for i in range(2, 6):
        matriz_labirinto[6][i] = 1
    for i in range(5, 7):
        matriz_labirinto[9][i] = 1
    for i in range(7, 10):
        matriz_labirinto[i][3] = 1

    return matriz_labirinto
    # imprime matriz


def imprime_matriz(matriz):
    print(np.matrix(matriz))
    print('\n')
    # cria um labirinto estático
class Node:
    def __init__(self, x, y, decisao, valor_heuristico):
        self.pos_x = x
        self.pos_y = y
        self.decisao = decisao
        self.distancia = valor_heuristico
#Classe agente

class Agente:

    # Construtor
    def __init__(self, labirinto):

        #Valor que representa o agente
        self.valor_agente = 2
        #Valor que representa o objetivo
        self.valor_objetivo = 3

        # Posição atual do Agente  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_atual_x = 0
        self.posicao_atual_y = 0

        #Labirinto que o agente terá que percorrer
        self.labirinto = labirinto

        #Posição inicial do Agente  na  matriz labirinto, onde x = linha e y = coluna
        self.localiza_agente()
        self.posicao_inicial_x = self.posicao_atual_x
        self.posicao_inicial_y = self.posicao_atual_y


        # Posição do objetivo  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_objetivo_y = 0
        self.posicao_objetivo_x = 0
        self.localiza_objetivo()

        #Cria uma matriz para colocar o valor dos custos
        self.matriz_de_custos = []
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(0)
            self.matriz_de_custos.append(linha)
        self.calcula_custo_total()

        #listas com as posicoes visitadas
        self.lista_visitados = []
    #Função que localiza a posição atual do agente
    def localiza_agente(self):
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 2:
                    self.posicao_atual_x = i
                    self.posicao_atual_y = j
                    print("Agente esta na posicao", self.posicao_atual_x,self.posicao_atual_y)
                    return
    # Função que localiza a posição atual do agente
    def localiza_objetivo(self):
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 3:
                    self.posicao_objetivo_x = i
                    self.posicao_objetivo_y = j
                    print("Objetivo esta na posicao", self.posicao_objetivo_x, self.posicao_objetivo_y)
                    return
    #Funções para movimentar o agente
    def andar_para_direita(self):
        #verifica se esta dentro dos limites da matriz
        if self.posicao_atual_y == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_y = self.posicao_atual_y + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2
            print("andou para direita")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)
            return True
    def andar_para_esquerda(self):
        # verifica se esta dentro dos limites da matriz
        if self.posicao_atual_y == 0:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_y = self.posicao_atual_y - 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2
            print("andou para esquerda")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

    def andar_para_cima(self):
        if self.posicao_atual_x == 0:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x - 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2
            print("andou para cima")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

    def andar_para_baixo(self):
        if self.posicao_atual_x == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2
            print("andou para baixo")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

    #Funções para verificar se os espaços estão livres ou não paredes
    def verifica_direita(self):
        if self.posicao_atual_y == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 1:
            #print("Pode andar para direita")
            return 1
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 0:
            #print("OPS! Parede")
            return 0
    def verifica_esquerda(self):
        if self.posicao_atual_y == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 1:
            #print("Pode andar para esquerda")
            return 1
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 0:
            #print("OPS! Parede")
            return 0

    def verifica_em_cima(self):
        if self.posicao_atual_x == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 1:
            #print("Pode andar para cima")
            return 1
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x -1][self.posicao_atual_y] == 0:
            #print("OPS! Parede")
            return 0

    def verifica_em_baixo(self):
        if self.posicao_atual_x == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 1:
            #print("Pode andar para baixo")
            return 1
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 3:
            #print("Você chegou no Objetivo! Parabéns")
            return 3
        if self.labirinto[self.posicao_atual_x +1][self.posicao_atual_y] == 0:
            #print("OPS! Parede")
            return 0
    def verifica_tudo(self):
        possiveis_caminhos = Fila_de_prioridade
        if self.verifica_direita() == 1:
            self.busca_lista_visitados(self.posicao_atual_x, self.posicao_atual_y + 1) == False;
            possiveis_caminhos.append(self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y + 1])
        if self.verifica_esquerda() == 1:
            self.busca_lista_visitados(self.posicao_atual_x, self.posicao_atual_y - 1) == False;
            possiveis_caminhos.append(self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y - 1])
        if self.verifica_em_cima() == 1:
            self.busca_lista_visitados(self.posicao_atual_x -1, self.posicao_atual_y) == False;
            possiveis_caminhos.append(self.matriz_de_custos[self.posicao_atual_x - 1][self.posicao_atual_y])
        if self.verifica_em_baixo() == 1:
            self.busca_lista_visitados(self.posicao_atual_x + 1, self.posicao_atual_y) == False;
            possiveis_caminhos.append(self.matriz_de_custos[self.posicao_atual_x + 1][self.posicao_atual_y])
        return possiveis_caminhos

    def busca_lista_visitados(self,node):
        for i in range(len(self.lista_visitados)):
            if self.lista_visitados == node:

                print("já Visitou esse lugar, procure outro!")
                return node
            else:
       # self.lista_visitados_x.append(x)
       # self.lista_visitados_y.append(y)
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
 #   def resultado(self):



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

 #   def busca_A(self,resultado):
 #       max_iteracoes = 100
 #       contador = 0
 #       if contador == max_iteracoes:
 #           return ValueError
 #       else:
  #          contador = contador + 1
   #     if self.verifica_direita() == 3 or self.verifica_esquerda() == 3 or self.verifica_em_cima() == 3 or self.verifica_em_baixo() == 3:
    #        print("Você saiu do labirinto")
     #       return
      #  else:
       #     return self.busca_A(self.resultado())

#função que calcula o valor euristico de cada nó
    def calcula_heuristica(self,x,y):
        distancia_x =  self.posicao_objetivo_x - x
        if distancia_x < 0:
            distancia_x = distancia_x * -1
        distancia_y =  self.posicao_objetivo_y - y
        if distancia_y < 0:
            distancia_y = distancia_y * -1
        distancia_heuristica = distancia_x + distancia_y
        if distancia_heuristica < 0:
            distancia_heuristica = distancia_heuristica * -1
        return distancia_heuristica

#Soma o custo heuristico com o calculo uniforme
    #OBS: ESSE CALCULO UNIFORME ESTA ERRADO. TEM QUE VER SE DÁ PARA CALCULAR FORA DA BUSCA
    def calcula_custo_total(self):
        #custo_uniforme = 0
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 1:
                    custo_heuristico = self.calcula_heuristica(i, j)
                    #chama
                    self.matriz_de_custos[i][j] = custo_heuristico
        print("Matriz de custo")
        imprime_matriz(self.matriz_de_custos)
