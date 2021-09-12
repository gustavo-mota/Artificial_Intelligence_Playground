from FormigasSolucao import *


class FormigasFeromonio:

    def __init__(self, n, evaporacao):
        self.P = evaporacao/100
        self.dimensao = n
        self.Matriz = []
        for i in range(n):
            # Original era 1
            self.Matriz.append([1000] * n)

    def __atualizacao__(self, formigueiro):
        self.__evaporacao__()
        self.__deposito__(formigueiro)

    def __evaporacao__(self):
        # vetor = list(map(lambda x: x.decisao(feromonio), formigueiro.formigueiro))
        # Experimentar dois maps aninhados
        # Experimentar substituir a matriz pelo retorno do map
        # map(lambda x: (round(i * (1 - self.P), 5) for i in x), self.Matriz)  # Test
        map(lambda x: ( map(lambda y: round(y * (1 - self.P), 5), x)), self.Matriz )
        #print(self.Matriz)
        '''for i in self.Matriz:
            i = [round(x * (1 - self.P), 5) for x in i]'''

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
                try:
                    # Custo mais fiel
                    '''self.Matriz[formigueiro.formigueiro[i].caminho[j]][j] += \
                        (formigueiro.formigueiro[i].Q / CalculaCustoCaminho(formigueiro.formigueiro[i]))'''
                    # Custo mais rápido
                    self.Matriz[ formigueiro.formigueiro[i].caminho[j] ][j] +=\
                                                (formigueiro.formigueiro[i].Q/self.dimensao)

                except:
                    print("Uma solução em potencial foi encontrada\n")
                    FormigasSolucao(formigueiro.formigueiro[i].caminho)
