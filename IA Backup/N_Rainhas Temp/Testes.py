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

print(m[])'''
