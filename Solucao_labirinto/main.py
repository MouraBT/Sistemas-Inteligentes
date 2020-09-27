import Busca_Labirinto_A as LF



labirinto = LF.cria_labirinto()
LF.imprime_matriz(labirinto)
agente_teste = LF.Agente(labirinto)
agente_teste.busca_caminho()

