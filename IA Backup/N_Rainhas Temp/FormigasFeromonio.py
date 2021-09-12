from FormigasSolucao import *


class FormigasFeromonio:

    def __init__(self, n, evaporacao):
        self.P = evaporacao/100
        self.dimensao = n
        self.Matriz = []
        for i in range(n):
            self.Matriz.append([1] * n)

    def __atualizacao__(self, formigueiro):
        self.__evaporacao__()
        self.__deposito__(formigueiro)

    def __evaporacao__(self):
        for i in self.Matriz:
            i = [round(x * (1 - self.P), 3) for x in i]

    '''def __evaporacao__(self):
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                self.Matriz[i][j] *= (1 - self.P)'''

    def __deposito__(self, formigueiro):
        for i in range(formigueiro.k):  # número de formigas
            for j in range(self.dimensao):  # n
                # adição
                # para cada coluna, captura a linha armazenada no caminho da formiga para adicionar o feromônio padrão
                # o Lk poderia ser uma heurística de peças se atacando em vez da dimensão
                '''self.Matriz[ formigueiro.formigueiro[i].caminho[j] ][j] +=\
                            (formigueiro.formigueiro[i].Q/self.dimensao)
                '''
                try:
                    self.Matriz[formigueiro.formigueiro[i].caminho[j]][j] += \
                        (formigueiro.formigueiro[i].Q / CalculaCustoCaminho(formigueiro.formigueiro[i]))
                except:
                    print("Uma solução em potencial foi encontrada\n")
                    FormigasSolucao(formigueiro.formigueiro[i].caminho)
