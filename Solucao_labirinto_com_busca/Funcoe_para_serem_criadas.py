#importa a biblioteca para usar fila
from collections import deque

#Classe labirinto
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
    #for i in range(1, 9):
    #    self.matriz_labirinto[i][5] = 1
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
    for i in range(4, 7):
        matriz_labirinto[9][i] = 1

class Node:
    # O custo é o valor que está na matriz
    def __init__(self, custo):
            self.custo = custo
            self.filho_esquerdo = None
            self.filho_direito = None

    def retorna_custo(self):
            return self.custo

    # A classe arvore conterá os nós e será criado a partir do nó raiz que é o estado inicial do agente. Ela será usado na busca
    # realizada pelo agente que encontrará o melhor caminho.
    # Classe arvore
class Arvore:
    def __init__(self, custo_raiz=None):
        # ver como faz polimorfismo ou a declaração para que raiz seja inicializado ja como Node
        if custo_raiz:
            self.raiz = Node(custo_raiz)
        else:
            self.raiz = None
        # ver se é melhor dentro do agente ou uma variável local da buscas
        self.lista_visitados = []
        self.tamanho_arvore = 0

    def insere_node(self,custo, arvore):
    # verifica se a arvore existe
        if arvore == None or node_pai == None:
            print("arvore ou nó invalidos")
            return None
        # caso arvore vazia
        if arvore.arvore_vazia() == True:
            arvore.raiz = custo
        # insere esquerda
        node_aux = Node(None)
        node_aux = arvore.raiz
        node_pai = Node(None)
        while node_aux != None:
            node_pai = aux
            if node_pai.filho_esquerdo != None and node_pai.filho_direito != None::
                node_aux = node_aux.filho_esquerdo
            if node_pai.filho_direito != None:
                node_aux = node_aux.filho_direito


    # insere direita
    # def deleta_node()
    # def deleta_arvore(self):
    def arvore_vazia(self):
        if (self.raiz == None):
            return True
        else:
            return False

    def ler_node_esquerdo(self, node_atual):
        return node_atual.filho_esquerdo

    def ler_node_direito(self, node_atual):
        return node_atual.filho_direito

    def procura_na_lista(self, node):
        for i in range(0, len(self.lista_visitados)):
            if (i == self.lista_visitados[i]):
                return True
        return False

    def guarda_node(self, node):
        if (self.procura_na_lista(self, node) == False):
            self.lista_visitados.append(node)
            return True
        else:
            return False

    def busca_profundida_da_arvore(self, node=None):
        if (node == None):
            return None
        if node.filho_esquerdo:
            self.busca_profundida(self, node.filho_esquerdo)
        if node.filho_direito:
            self.busca_profundida(self, node.filho_direito)
# O agente irá herda a árvore e ela será utilizado no metodo de busca dentro do agente



#Nessa função ele utiliza as funções de verificação. Primeiro ele verifica a direita se o caminho estiver livre ele verifica a matriz de custos
#e atribui o variável maior e decisao = 1. Se esquerda estiver livre e o valor da matriz de custos for maior que a variável  maior
#ele atualiza menor e muda a decisão. a função repete o mesmo procedimento para cima e para baixo.
#O valor da decisao final, a quem tem o menor valor de custo será o quadrado que o agente irá se movimentar.
#O movimento será feito pela chamada da função movimento
#decisao = 1 move para direita
# decisao = 2 move para esquerda
# decisao = 3 move para emcima
# decisao = 4 move para baixo
