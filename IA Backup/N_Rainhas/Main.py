import time
from FormigasFeromonio import *
from FormigasSolucao import *
from Formigas import *
from Exploracao import *
from TextFormater import *


def Main():
    dimensao = int(input("Digite a dimensao: "))
    evaporacao = int(input("Digite a taxa de evaporacao: "))  # de zero a cem
    feromonio = FormigasFeromonio(dimensao, evaporacao)
    formigasNumero = int(input("Insira o número de formigas: "))
    formigueiro = Formigueiro(formigasNumero, dimensao)
    modo = int(input("Insira o modo: ")) # Modo 4 requer par formigas
    #iteracao = int(input("Digite o número de iterações limite: "))
    Exploracao(1, feromonio, formigueiro, modo)
    print("Dimensão: ", dimensao,
          "Evaporação: ", evaporacao,
          "Formigas: ", formigasNumero)

start_time = time.time()
Main()
print("--- %s seconds ---" % (time.time() - start_time))
