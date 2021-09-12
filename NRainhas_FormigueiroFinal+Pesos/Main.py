import time
from FormigasFeromonio import *
from FormigasSolucao import *
from Formigas import *
from Exploracao import *


def Main():
    dimensao = int(input("Digite a dimensao: "))
    evaporacao = int(input("Digite a taxa de evaporacao: "))  # de zero a cem
    feromonio = FormigasFeromonio(dimensao, evaporacao)
    formigasNumero = int(input("Insira o número de formigas: "))
    formigueiro = Formigueiro(formigasNumero, dimensao)
    #modo = int(input("Insira o modo: ")) # Modo 4 requer par formigas
    modo = 3
    #iteracao = int(input("Digite o número de iterações limite: "))
    start_time = time.time()
    Exploracao(feromonio, formigueiro, modo)
    print("Dimensão: ", dimensao,
          "Evaporação: ", evaporacao,
          "Formigas: ", formigasNumero)
    print("--- %s seconds ---" % (time.time() - start_time))

Main()
