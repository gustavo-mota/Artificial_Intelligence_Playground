import math
import copy


def FormigasSolucao(caminho):
    solucao = []
    for i in range(len(caminho)):
        solucao.append([0] * len(caminho))
    for j in range(len(caminho)):
        solucao[caminho[j]][j] = 1
    for k in range(len(caminho)):
        print(solucao[k])


def Porcentagem(vetor):
    return round(sum(vetor)/len(vetor), 2)  # vetor de binário


def ExclusaoLinha(vetor, retas):
    roleta = copy.deepcopy(vetor)
    for i in range(len(roleta)):
        if i in retas:
            roleta[i] = 0.0
    # sorteado = Roleta(roleta)
    # retas.append(sorteado)
    return roleta


# para calcular depósito
def CalculaCustoCaminho(formiga):
    Ataque = 0

    for i in range(len(formiga.caminho)):
        for j in range(len(formiga.caminho)):
            D = i - j
            if D!=0:
                # diagonal direita
                if D < 0:
                    # j frente i
                    D *= -1
                    # linha igual
                    if formiga.caminho[i] == formiga.caminho[j]:
                        Ataque += 1
                    # desce
                    if formiga.caminho[i]+D == formiga.caminho[j]:
                        Ataque += 1
                    # sobe
                    if formiga.caminho[i]-D == formiga.caminho[j]:
                        Ataque += 1
                # diagonal esquerda
                elif D > 0:
                    # j atrás i
                    # linha igual
                    if formiga.caminho[i] == formiga.caminho[j]:
                        Ataque += 1
                    # desce
                    if formiga.caminho[i] + D == formiga.caminho[j]:
                        Ataque += 1
                    # sobe
                    if formiga.caminho[i] - D == formiga.caminho[j]:
                        Ataque += 1

    '''caminho = copy.deepcopy(formiga.caminho)
    for colunaAtual, linhaAtual in enumerate(caminho):
        #colunaAtual = caminho.index(x)
        caminho.remove(linhaAtual)
        for colunaAtaque, linhaAtaque in enumerate(caminho):
            # colunaAtaque = caminho.index(y)
            if abs(colunaAtual - colunaAtaque) == abs(int(linhaAtual) - int(linhaAtaque)):
                Ataque += 1'''
    # aboluto(coluna atual - coluna ataque) = absoluto(linha atual - linha ataque)
    return Ataque**5

