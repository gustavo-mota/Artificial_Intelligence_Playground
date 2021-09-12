import time
import numpy

'''A = []
for i in range(5):
    A.append( [0] * 5 )

A[1][1] = 2
A[1][1] = 0
print(A)'''

'''
A = []
for i in range(5):
    A.append( [1] * 5 )

for k in range(5):
    for j in range(5):
       A[k][j] *= (1 - 0.80)

print(A)'''

'''Caminho = [1,3,0,2]

Ataque = 0
for i in range(2):
    for j in range(2):
        D = i - j
        if D!=0:
            # diagonal direita
            if D < 0:
                # j frente i
                D *= -1
                # linha igual
                if Caminho[i] == Caminho[j]:
                    Ataque += 1
                # desce
                if Caminho[i] + D == Caminho[j]:
                    Ataque += 1
                # sobe
                if Caminho[i] - D == Caminho[j]:
                    Ataque += 1
            # diagonal esquerda
            elif D > 0:
                # j atrás i
                # linha igual
                if Caminho[i] == Caminho[j]:
                    Ataque += 1
                # desce
                if Caminho[i] + D == Caminho[j]:
                    Ataque += 1
                # sobe
                if Caminho[i] - D == Caminho[j]:
                    Ataque += 1
print(Ataque)'''

'''caminho = [0] * 5
print(caminho)'''

'''x = int(input())
try:
    print(x/0)
except:
    x *= 1
    print(x)'''

'''m = numpy.array([ [0,1,2,3],
        [0,1,2,3],
        [0,1,2,3],
        [0,1,2,3]
    ])

print(m.transpose()[0])'''

#print(round(0.00000700002, 3))

'''m = [ [0,1,2,3],
      [0,1,2,3],
      [0,1,2,3],
      [0,1,2,3]
    ]
m = list(zip(*m))
m[1] = list(m[1])
print(m)'''

'''lista = (1,0,1,0)
lista = list(lista)
print(lista)'''

'''elif modo == 4:
        # modo thread
        i = 0
        whileVar = 1
        formiga = -1
        while (True):
            for f in formigueiro.formigueiro:
                    f = Thread(target=Formiga,args=[formigueiro.dimensao])
                    f.start()
            # Verificar se cria todas as formigas ao mesmo tempo e as deixa rodando mesmo após
            '''
'''for f2 in range(formigueiro.k):
    formigueiro.formigueiro[f2].start()'''
'''


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
FormigasSolucao(formigueiro.formigueiro[formiga].caminho)'''

'''time.sleep(5)
print(5)'''

'''x = 0
for i in range(11):
    x += 0.3
print(x)'''