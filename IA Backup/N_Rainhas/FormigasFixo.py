import copy
from Roleta import *
from FormigasSolucao import *

class Formigueiro:
    def __init__(self, numeroDeFormigas, dimensao):
        self.formigueiro = []
        self.k = numeroDeFormigas
        self.dimensao = dimensao

        # criação iterativa de formigas diferentes
        for i in range(self.k):
            self.formigueiro.append(Formiga(dimensao, i))

class Formiga:
    def __init__(self, num):
        self.caminho = [
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
            -1, -1, -1, -1,
        ]
        self.Q = 10
        self.dimensao = 40
        self.num = num


    def __decisao__(self, MatrizFeromonio):
        transposta = list(zip(*MatrizFeromonio.Matriz))
        retas = []
        indice = -1
        for j in transposta:
            indice +=1
            #print(type(transposta[0]))
            d = len(transposta)
            j = list(j)
            j[:] = [float(i)/d for i in j]

            # Exclusão de linha
            roleta = copy.deepcopy(j)
            for i in range(len(roleta)):
                if i in retas:
                    # print("sim")
                    roleta[i] = 0.0
            sorteado = Roleta(roleta)
            retas.append(sorteado)

            # Exclusão de linha fim
            self.caminho[indice] = sorteado

            # self.caminho[indice] = Roleta(j)
            if CalculaCustoCaminho(self) == 0:
                print("Solução em potencial achada, decisão formiga: ", self.num)
                return 1

        return 0
