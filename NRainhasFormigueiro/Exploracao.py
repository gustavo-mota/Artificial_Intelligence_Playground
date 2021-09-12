from FormigasSolucao import *

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
        whileVar = 1
        formiga = -1
        while(True):
            for f in range(formigueiro.k):
                # Still needing tests
                # It can need try and exception
                teste = formigueiro.formigueiro[f].__decisao__(feromonio)
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
    else:
        print("Tente uma opção válida")
