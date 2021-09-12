import copy
from Roleta import *
from FormigasSolucao import *
from threading import Thread

class Formigueiro:
    def __init__(self, numeroDeFormigas, dimensao):
        self.formigueiro = []
        self.k = numeroDeFormigas
        self.dimensao = dimensao

        # criação iterativa de formigas diferentes
        for i in range(self.k):
            self.formigueiro.append(Formiga(dimensao, i))
            #self.formigueiro.append(ThreadedFormiga(dimensao, i))



class ThreadedFormiga(Thread):

    def __init__(self, dimensao, num):
        Thread.__init__(self)
        self.caminho = [-1]*dimensao
        self.Q = 10
        self.dimensao = dimensao
        self.num = num

    # Decisão
    def __run__(self, MatrizFeromonio):
        transposta = copy.deepcopy(list(zip(*MatrizFeromonio.Matriz)))
        retas = []
        indice = -1
        for j in transposta:
            indice +=1
            #print(type(transposta[0]))
            d = len(transposta)
            j = list(j)
            j[:] = [float(i)/d for i in j]

            # Exclusão de linha
            # não ta acontecendo

            roleta = copy.deepcopy(j)
            #print(roleta)
            for i in range(len(roleta)):
                if i in retas:
                    #print("sim")
                    roleta[i] = 0.0
            sorteado = Roleta(roleta)
            #print(roleta)
            #print(sorteado)
            retas.append(sorteado)
            #print(retas)
            # Exclusão de linha fim
            self.caminho[indice] = sorteado

            # self.caminho[indice] = Roleta(j)
            if CalculaCustoCaminho(self) == 0:
                print("Solução em potencial achada, decisão formiga: ", self.num)
                return 1

        return 0

class Formiga:
    def __init__(self, dimensao, num):
        self.caminho = [-1]*dimensao
        self.Q = 10
        self.dimensao = dimensao
        self.num = num

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

    '''def __decisao__(self, MatrizFeromonio):
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

        return 0'''

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
