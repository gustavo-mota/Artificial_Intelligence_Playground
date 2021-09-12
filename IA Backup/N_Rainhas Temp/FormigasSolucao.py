def FormigasSolucao(caminho):
    solucao = []
    for i in range(len(caminho)):
        solucao.append([0] * len(caminho))
    for j in range(len(caminho)):
        solucao[caminho[j]][j] = 1
    for k in range(len(caminho)):
        print(solucao[k])

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

    return Ataque

