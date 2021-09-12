# Apenas para matrizes de dimensões ímpares
class Matriz:
    def __init__(self, dimensao):
        self.dimensao = dimensao
        self.matriz = []
        for i in range(0, dimensao):
            self.matriz.append([0] * dimensao)
        self.a = 1
        self.b = 3

    def __ls__(self):
        #self.matriz[0][0] = 0
        #self.matriz[0][1] = 1
        #self.matriz[1][0] = 3
        for i in range(0, self.dimensao):
            for j in range(0, self.dimensao):
                self.matriz[i][j] = (i * self.b + j * self.a) % self.dimensao

    def __ctnq__(self, valor):
        if self.dimensao % 2 != 0:
            for i in range(0,self.dimensao):
                for j in range(0,self.dimensao):
                    if self.matriz[i][j] == valor:
                        self.matriz[i][j] = 1
                    else:
                        self.matriz[i][j] = 0
        else: # par
            #self.matriz[1][0] = 1
            it = -1
            for i in range(self.dimensao):
                try:
                    print(self.matriz[it+2][i])
                    self.matriz[it+2][i] = 1
                    it += 2
                except:
                    break
            it = -1
            start = int(self.dimensao/2)
            for j in range(start, self.dimensao):
                try:
                    print(self.matriz[it + 1][j])
                    self.matriz[it+1][j] = 1
                    it += 2
                except:
                    break
            for k in range(self.dimensao):
                for l in self.matriz[k]:
                    if l != 1:
                        l = 0

    def __colision__(self):
        lista = []
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                if self.matriz[j][i] ==1:
                    lista.append(j)
                    #lista.append(self.matriz[i].index(1))
        Ataque = 0
        for i in range(self.dimensao):
            for j in range(self.dimensao):
                if abs(i - j) == abs(lista[i] - lista[j]) and lista[i]!=lista[j]:
                    Ataque+=1
        print(Ataque)
        print(lista)

    def __print__(self):
        for i in range(0, self.dimensao):
            print(self.matriz[i], "\n")


def Main():
    tuple = (int(input("Digite a dimensão: ")), int(input("Digite o valor: ")))

    matriz = Matriz(tuple[0])
    matriz.__ls__()
    matriz.__print__()
    matriz.__ctnq__(tuple[1])
    print("\n")
    matriz.__print__()
    matriz.__colision__()

Main()