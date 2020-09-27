import numpy as np

######################Funções Do Labirinto###################################################
#Cria Labirinto
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
    #for i in range(7, 10):
    #    matriz_labirinto[i][3] = 1

    return matriz_labirinto
    # imprime matriz

#Funcao para imprimir o labirinto
def imprime_matriz(matriz):
    print(np.matrix(matriz))
    print('\n')
    # cria um labirinto estático

#######################################Funções e classe do AGENTE##########################################
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

        # Posição do objetivo  na  matriz labirinto, onde x = linha e y = coluna
        self.posicao_objetivo_y = 0
        self.posicao_objetivo_x = 0
        self.localiza_objetivo()

        #Cria uma matriz para colocar o valor dos custos
        self.matriz_de_custos = []
        self.inicializa_matriz_de_custos()
        self.calcula_custo_total()

        #listas com as posicoes visitadas
        self.lista_visitados_x = []
        self.lista_visitados_y = []
        self.lista_visitados_x.append(self.posicao_atual_x)
        self.lista_visitados_y.append(self.posicao_atual_y)

        #Variáveis para controlar Bifurcações
        self.entrada_bifurcacao_x = 0
        self.entrada_bifurcacao_y = 0

        #Lista movimentos finais
        self.fila_final = []

        #Fila de prioridades de uma caminho possivel
        self.fila_temp = []

        #Fila dos caminhos da bifuracação com os valores heuristicos
        self. caminho_possiveis = []

        #Variavel de controle se ele esta tentando um caminho da bifurcação
        self.na_bifurcacao = False

        #varialve de controle se chegou no objetivo
        self.chegou_objetivo = 0
######################Funções de Localização############################################
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

######################Funções de Verificação############################################
    #Verifica Lista Visitados
    def busca_lista_visitados(self, x, y):
        for i in range(len(self.lista_visitados_x)):
            if self.lista_visitados_x[i] == x and self.lista_visitados_y[i] == y:
                #print("já Visitou esse lugar, procure outro!")
                return True

        return False

    #Verifica Se chegou no objetivo
 #   def se_objetivo(self):
 #       if self.posicao_atual_x == self.posicao_objetivo_x and self.posicao_atual_y == self.posicao_objetivo_y:
 #           return True
 #       else:
 #           return False

    #Verificações se pode andar para os lados
    # Primeiro verifica se pode é um espaço andável ou parede ou o objetivo.
    # Depois verifica se já visitou esse lugar
    # Retorna:
    # False Se não puder andar
    # True  Se puder andar(quando a valor da posição do labirinto é 1 ou 3)

    def verifica_direita(self):
        if self.posicao_atual_y == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 1:
            if self.busca_lista_visitados(self.posicao_atual_x, self.posicao_atual_y +1) == True:
                return False
            else:
                #print("Pode andar para direita")
                return True
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y + 1] == 3:
            return True

    def verifica_esquerda(self):
        if self.posicao_atual_y == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 1:
            if self.busca_lista_visitados(self.posicao_atual_x, self.posicao_atual_y - 1) == True:
                return False
            else:
                #print("Pode andar para esquerda")
                return True
        if self.labirinto[self.posicao_atual_x][self.posicao_atual_y - 1] == 3:
            return True
    def verifica_em_cima(self):
        if self.posicao_atual_x == 0:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 1:
            if self.busca_lista_visitados(self.posicao_atual_x - 1, self.posicao_atual_y) == True:
                return False
            else:
                #print("Pode andar para cima")
                return True
        if self.labirinto[self.posicao_atual_x - 1][self.posicao_atual_y] == 3:
            return True
    def verifica_em_baixo(self):
        if self.posicao_atual_x == 9:
            #print("Cuidado! Vcê atingiu o limite do labirinto")
            return False
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 1:
            if self.busca_lista_visitados(self.posicao_atual_x + 1, self.posicao_atual_y) == True:
                return False
            else:
                #print("Pode andar para baixo")
                return True
        if self.labirinto[self.posicao_atual_x + 1][self.posicao_atual_y] == 3:
            return True

    #Função que verifica os caminhos possíveis
    #Verifica todos os lados se puder andar adiciona na lista ordenada do memor para o maior valor heuristico
    #de caminho possiveis e coma decisao:
    #EX: caminhos_possiveis = [[5,1], [9,4]] o agente pode andar para direita(1) e baixo(4) os valores heuristico
    #são respectivamente 5 e 9.
    #O tamanho da lista vai indicar quantos caminho eu posso seguir.
    def verifica_todos_os_lados(self):
        #limpa a lista de caminhos possiveis a cada nova verificação
        if len(self.caminho_possiveis) != 0:
            self.caminho_possiveis.clear()

        #verifica Todos os lados
        direita = self.verifica_direita()
        esquerda = self.verifica_esquerda()
        em_cima = self.verifica_em_cima()
        em_baixo= self.verifica_em_baixo()

        #Se ele puder mover o valor sera verdadeiro, a heuristica será calculada e acrescenta no caminhos possiveis
        if direita == True:
            valor_h = self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y + 1]
            decisao = [valor_h, 1]
            self.insere_ordenado(decisao)

        if esquerda == True:
            valor_h = self.matriz_de_custos[self.posicao_atual_x][self.posicao_atual_y - 1]
            decisao = [valor_h, 2]
            self.insere_ordenado(decisao)

        if em_cima == True:
            valor_h = self.matriz_de_custos[self.posicao_atual_x - 1][self.posicao_atual_y]
            decisao = [valor_h, 3]
            self.insere_ordenado(decisao)

        if em_baixo == True:
            valor_h = self.matriz_de_custos[self.posicao_atual_x + 1][self.posicao_atual_y]
            decisao = [valor_h, 4]
            self.insere_ordenado(decisao)

        #Se existe algum caminho possivel e um deles tem heuristica 0 quer dizer que atingiu o objetivo(basta andar para onde é 0)
        if len(self.caminho_possiveis) != 0:
            if self.caminho_possiveis[0][0] == 0:
                self.chegou_objetivo = self.valor_objetivo



#####################Funções Para movimentar o Agente#################################
    # A funções andar movem o agente para o respectivo lad0.
    # Onde que ele esta passa a ser 1 e atualiza a posição atual que passa a ser 2
    # Adiciona na Lista de visitados
    # Retorna False se não consegui andar e True se conseguiu


    def andar_para_direita(self):

        #verifica se esta dentro dos limites da matriz
        if self.posicao_atual_y == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            #atualiza o valor no labirinto
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_y = self.posicao_atual_y + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

            #Atualiza a lista de visitados
            self.lista_visitados_x.append(self.posicao_atual_x)
            self.lista_visitados_y.append(self.posicao_atual_y)

            #Imprimi
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

            # Atualiza a lista de visitados
            self.lista_visitados_x.append(self.posicao_atual_x)
            self.lista_visitados_y.append(self.posicao_atual_y)

            # Imprimi
            print("andou para esquerda")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

            return True
    def andar_para_cima(self):

        if self.posicao_atual_x == 0:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x - 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

            # Atualiza a lista de visitados
            self.lista_visitados_x.append(self.posicao_atual_x)
            self.lista_visitados_y.append(self.posicao_atual_y)

            # Imprimi
            print("andou para cima")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

            return True
    def andar_para_baixo(self):

        if self.posicao_atual_x == 9:
            print("Cuidado! Vcê atingiu o limite do labirinto")
            return False

        else:
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 1
            self.posicao_atual_x = self.posicao_atual_x + 1
            self.labirinto[self.posicao_atual_x][self.posicao_atual_y] = 2

            # Atualiza a lista de visitados
            self.lista_visitados_x.append(self.posicao_atual_x)
            self.lista_visitados_y.append(self.posicao_atual_y)

            # Imprimi
            print("andou para baixo")
            print("Labirinto Estado Atual")
            imprime_matriz(self.labirinto)

            return True

    #Função que movimenta de acordo com a decisão do agente.
    # 1 = Direita
    # 2 = Esquerda
    # 3 = Para cima
    # 4 = Para Baixo
    def movimenta(self, decisao):
        if decisao == 1:
            self.andar_para_direita()
        if decisao == 2:
            self.andar_para_esquerda()
        if decisao == 3:
            self.andar_para_cima()
        if decisao == 4:
            self.andar_para_baixo()

##################### Funções Para Busca A* #################################

    #Função que calcula a distância para o objetivo
    def calcula_heuristica(self, x, y):
        distancia_x = self.posicao_objetivo_x - x
        if distancia_x < 0:
            distancia_x = distancia_x * -1
        distancia_y = self.posicao_objetivo_y - y
        if distancia_y < 0:
            distancia_y = distancia_y * -1
        distancia_heuristica = distancia_x + distancia_y
        if distancia_heuristica < 0:
            distancia_heuristica = distancia_heuristica * -1
        return distancia_heuristica

    #Função Busca A*
    def busca_caminho(self):
        while self.chegou_objetivo == 0:
            #Verificação se pode andar
            self.verifica_todos_os_lados()

            #Condição de um unico caminho
            #O agente fica no loop até achar uma bifurcação
            while len(self.caminho_possiveis) == 1 and self.chegou_objetivo == 0:
                if not self.na_bifurcacao:
                    #Decisao do caminho e colocou na fila de caminho final
                    self.fila_final.append(self.caminho_possiveis[0][1])

                else:
                    self.fila_temp.append(self.caminho_possiveis[0][1])

                self.movimenta(self.caminho_possiveis[0][1])
                self.verifica_todos_os_lados()
            #Caso que esta na bifurcação e escolhe um caminho
            #A partir dai os valores serão colocados em uma lista temporaria, para caso ele atingir um ponto
            #em que o agente não pode andar para mais nenhum lado poder voltar
            if len(self.caminho_possiveis) > 1:
                self.entrada_bifurcacao_x = self.posicao_atual_x
                self.entrada_bifurcacao_y = self.posicao_atual_y
                self.na_bifurcacao = True
                self.movimenta(self.caminho_possiveis[0][1])
                self.fila_temp.append(self.caminho_possiveis[0][1])

            #Chegou no objetivo.
            if self.chegou_objetivo == 3:
                i = 0
                #Coloca a lista  temporaria na final para ter os passos do Agente
                while len(self.fila_temp) != 0:
                    self.fila_final.append(self.fila_temp[0])
                    self.fila_temp.pop(0)
                    i += 1

            #O agente está preso e então o valor atual recebe o da ultima bifurcação
            #e limpa a ista temporaria
            if len(self.caminho_possiveis) == 0:
                #volta para a bifurcacao
                self.posicao_atual_x = self.entrada_bifurcacao_x
                self.posicao_atual_y = self.entrada_bifurcacao_y

                #limpa fila temporaria
                self.fila_temp.clear()
                self.na_bifurcacao = False

        self.movimenta(self.caminho_possiveis[0][1])
        print("Parabéns! Você saiu do labirinto")




#######################Funções extras Auxiliares########################################
#Função para inicializa a matriz de custos
    def inicializa_matriz_de_custos(self):
        for i in range(10):
            linha = []
            for j in range(10):
                linha.append(0)
            self.matriz_de_custos.append(linha)

    def insere_ordenado(self, valor):
        if len(self.caminho_possiveis) == 0:
            self.caminho_possiveis.append(valor)
        else:
            i = 0
            #menor = self.caminho_possiveis[0][0]
            while valor[0] >= self.caminho_possiveis[i][0]:
                i += 1
                if i >= len(self.caminho_possiveis):
                    break
               # menor = self.caminho_possiveis[i][0]
            self.caminho_possiveis.insert(i, valor)
        print("caminhos possiveis", self.caminho_possiveis)

    #Calcula o valor heuristico de cada posicao que eu posso anda
    def calcula_custo_total(self):
        # custo_uniforme = 0
        for i in range(10):
            for j in range(10):
                if self.labirinto[i][j] == 1:
                    custo_heuristico = self.calcula_heuristica(i, j)
                    # chama
                    self.matriz_de_custos[i][j] = custo_heuristico
        print("Matriz de custo")
        imprime_matriz(self.matriz_de_custos)
