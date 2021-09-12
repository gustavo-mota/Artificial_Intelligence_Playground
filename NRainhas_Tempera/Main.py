import numpy as np
import math as mt
import random as rd

def GeraNo(dimensao):
    return np.arange(dimensao)

def GeraVizinho(array, dimensao):
    array[rd.randint(dimensao)] = rd.randint(dimensao)
    return array

def Colisoes(array):
    ataques = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if abs(i - j) == abs(array[i] - array[j]):
                ataques += 1
    return ataques

def Probabilidade(array1, array2, num):
    return None

def TemperaSimulada(dimensao, C, max):
    atual = GeraNo(dimensao)
    for i in range(max):
        t = np.arange(1, max)
        T = C/mt.sqrt(t)
        viz = GeraVizinho(atual, dimensao)
        P_atual = Colisoes(atual)
        P_viz = Colisoes(viz)
        '''if  P_viz <= P_atual:
            atual = viz'''
        if t <= 0.005 or P_atual == 0:
            return atual
        else:
            atual = Probabilidade(atual, viz, T)
    return atual

vetor = [1,1]
print(set(vetor))