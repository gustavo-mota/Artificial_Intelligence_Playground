from threading import Thread
from FormigasSolucao import *
from Formigas import *


def Exploracao(feromonio, formigueiro, modo):
    if modo == 3:
        # modo direto
        i = 0
        while(True):
            vetor = list(map(lambda x: x.decisao(feromonio), formigueiro.formigueiro))
            print(vetor)
            # vetor = map(lambda x: x.d(matriz), formigueiro)
            if 1 in vetor:
                f = vetor.index(1)
                print("Solução achada pela formiga ", f)
                FormigasSolucao(formigueiro.formigueiro[f].caminho)
                break
            feromonio.__atualizacao__(formigueiro)
            print("Iteração ", i, "terminada\n")
            i += 1
    else:
        print("Tente uma opção válida")