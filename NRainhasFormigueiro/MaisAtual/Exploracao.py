from threading import Thread
from FormigasSolucao import *
from Formigas import *

def Exploracao(iteracao, feromonio, formigueiro, modo):
    if modo == 1:
        # modo acompanhando
        print("Não implementado")
    elif modo == 2:
        # modo direto
        for i in range(iteracao):
            for f in range(formigueiro.k):
                # Still needing tests
                # It can need try and exception
                formigueiro.formigueiro[f].__decisao__(feromonio)
            feromonio.__atualizacao__(formigueiro)
            print("Iteração ", i, "terminada\n")
    elif modo == 3:
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
    elif modo == 4:
        # modo thread
        i = 0
        whileVar = 1
        formiga = -1
        while (True):
            for f in formigueiro.formigueiro:
                f = Thread(target=f.__decisao__(feromonio),args=[formigueiro.dimensao])
                f.start()
            # Verificar se cria todas as formigas ao mesmo tempo e as deixa rodando mesmo após
            for f2 in formigueiro.formigueiro:
                teste = CalculaCustoCaminho(f2)
                if teste == 1:
                    print("Solução em potencial encontrada, Exploração\n")
                    formiga = f2
                    whileVar = 0
                    break
            if whileVar == 0:
                break
            feromonio.__atualizacao__(formigueiro)
            print("Iteração ", i, "terminada\n")
            i += 1
        print("Solução achada pela formiga ", formiga)
        FormigasSolucao(formigueiro.formigueiro[formiga].caminho)

    else:
        print("Tente uma opção válida")
    '''while(True):
            for f in range(formigueiro.k):
                vetor = map(lambda x: x.decisao(feromonio), formigueiro.formigueiro)
                # Still needing tests
                # It can need try and exception
                teste = formigueiro.formigueiro[f].decisao(feromonio)
                # vetor = map(lambda x: x.d(matriz), formigueiro)
                if teste == 1:
                    print("Solução em potencial encontrada, Exploração\n")
                    formiga = f
                    whileVar = 0
                    break
            if whileVar == 0:
                break
            feromonio.__atualizacao__(formigueiro)
            print("Iteração ", i, "terminada\n")
            i += 1
        print("Solução achada pela formiga ", formiga)
        FormigasSolucao(formigueiro.formigueiro[formiga].caminho)
'''