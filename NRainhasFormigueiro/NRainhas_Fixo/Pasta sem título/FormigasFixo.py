import copy
from Roleta import *
from FormigasSolucao import *
from FormigasFeromonio import *
from Colunas import *

'''class Formigueiro:
    def __init__(self, numeroDeFormigas, dimensao):
        self.formigueiro = []
        self.k = numeroDeFormigas
        self.dimensao = dimensao

        # criação iterativa de formigas diferentes
        for i in range(self.k):
            self.formigueiro.append(Formiga(dimensao, i))'''

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
        self.Q = 10 # Alterar esse valor implica em alterar em deposito
        self.dimensao = 40
        self.num = num

    def __decisao__(self, MatrizFeromonio):
        self.caminho = [Roleta(Coluna(MatrizFeromonio.Matriz, 0)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 1)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 2)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 3)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 4)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 5)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 6)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 7)),

                        Roleta(Coluna(MatrizFeromonio.Matriz, 8)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 9)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 10)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 11)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 12)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 13)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 14)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 15)),

                        Roleta(Coluna(MatrizFeromonio.Matriz, 16)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 17)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 18)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 19)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 20)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 21)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 22)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 23)),

                        Roleta(Coluna(MatrizFeromonio.Matriz, 24)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 25)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 26)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 27)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 28)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 29)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 30)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 31)),

                        Roleta(Coluna(MatrizFeromonio.Matriz, 22)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 33)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 34)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 35)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 36)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 37)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 38)),
                        Roleta(Coluna(MatrizFeromonio.Matriz, 39))
                        ]

        if CalculaCustoCaminho(self) == 0:
            print("Solução em potencial achada, decisão formiga: ", self.num)
            FormigasSolucao(self.caminho)
            return 1

        return self.caminho


    def __decisao2__(self, MatrizFeromonio):
        # transposta = list(zip(*MatrizFeromonio.Matriz))
        retas = []
        indice = -1
        for k in range(40):
            indice += 1
        #for j in transposta:
            '''
            indice +=1
            #print(type(transposta[0]))
            d = 40
            j = list(j)
            j[:] = [float(i)/d for i in j]
            '''

            # Exclusão de linha
            '''roleta = copy.deepcopy(Coluna(MatrizFeromonio.Matriz, k))
            for i in range(40):
                if i in retas: # Conferir
                    # print("sim")
                    roleta[i] = 0.0
            sorteado = Roleta(roleta)
            retas.append(sorteado)
            # Exclusão de linha fim
            self.caminho[indice] = sorteado'''
            # Sem exclusão de linha
            self.caminho[indice] = Roleta(Coluna(MatrizFeromonio.Matriz, k))
            if CalculaCustoCaminho(self) == 0:
                print("Solução em potencial achada, decisão formiga: ", self.num)
                FormigasSolucao(self.caminho)
                return 1

        return self.caminho
