from FormigasSolucao import *
#from past.builtins import xrange  #external library

def CaminhoJulgamento(formigacaminho, pecas):
    ataques = CalculaCustoCaminho(formigacaminho)
    if ataques > pecas:
        return 0
    return 1


class FormigasFeromonio:

    def __init__(self, n, evaporacao):
        self.P = evaporacao/100
        self.dimensao = n
        self.Matriz = []
        for i in range(n):
            # Original era 1
            self.Matriz.append([(1000, [])] * n)  # Tupla

    def __atualizacao__(self, formigueiro):
        self.__evaporacao__()
        self.__deposito__(formigueiro)

    def __evaporacao__(self):
        # vetor = list(map(lambda x: x.decisao(feromonio), formigueiro.formigueiro))
        # Experimentar dois maps aninhados
        # Experimentar substituir a matriz pelo retorno do map
        # map(lambda x: (round(i * (1 - self.P), 5) for i in x), self.Matriz)  # Test
        map(lambda linha: ( map(lambda tupla: round(tupla[0] * (1 - self.P), 5), linha)), self.Matriz )
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

                    alpha = Porcentagem(self.Matriz[formigueiro.formigueiro[i].caminho[j]][j][1])  # Bom
                    betha = 1 - alpha  # Ruim

                    self.Matriz[formigueiro.formigueiro[i].caminho[j]][j][0] += \
                        (formigueiro.formigueiro[i].Q**alpha / CalculaCustoCaminho(formigueiro.formigueiro[i])**betha)
                    # Custo mais rápido
                    '''self.Matriz[ formigueiro.formigueiro[i].caminho[j] ][j] +=\
                                                (formigueiro.formigueiro[i].Q/self.dimensao)'''

                except:
                    print("Uma solução em potencial foi encontrada\n")
                    FormigasSolucao(formigueiro.formigueiro[i].caminho)

    def __CaminhoHistorico__(self, formigacaminho, pecas):
        julgo = CaminhoJulgamento(formigacaminho, pecas)
        for linha in formigacaminho.caminho:
            self.Matriz[linha][formigacaminho.caminho.index(linha)][1].append(julgo)
