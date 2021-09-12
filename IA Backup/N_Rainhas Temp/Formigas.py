from Roleta import *
from FormigasSolucao import *

class Formigueiro:
    def __init__(self, numeroDeFormigas, dimensao):
        self.formigueiro = []
        self.k = numeroDeFormigas

        # criação iterativa de formigas diferentes
        for i in range(self.k):
            self.formigueiro.append(Formiga(dimensao))


class Formiga:
    def __init__(self, dimensao):
        self.caminho = [-1]*dimensao
        self.Q = 1
        self.dimensao = dimensao

    '''def __decisao__(self, MatrizFeromonio):
        Coluna = []
        # Coluna i
        for i in range(MatrizFeromonio.dimensao):
            # Linha j
            for j in range(MatrizFeromonio.dimensao):
                # calcula probabilidade com custo baseado em dimensão
                Coluna.append(MatrizFeromonio.Matriz[j][i]/MatrizFeromonio.dimensao)
            # Roleta retorna índice correspondente a linha
            self.caminho[i] = Roleta(Coluna)

            if CalculaCustoCaminho(self) == 0:
                print("Solução em potencial achada, decisão\n")
                return 1

            # Zerou Coluna
            Coluna = []
        # return self.caminho
        return 0'''

    def __decisao__(self, MatrizFeromonio):
        transposta = []
        for i in range(MatrizFeromonio.dimensao):
            transposta.append([row[i] for row in MatrizFeromonio.Matriz])
        indice = -1
        for j in transposta:
            indice +=1
            d = len(transposta)
            j[:] = [float(i)/d for i in j]
            self.caminho[indice] = Roleta(j)

            if CalculaCustoCaminho(self) == 0:
                print("Solução em potencial achada, decisão\n")
                return 1

        return 0
