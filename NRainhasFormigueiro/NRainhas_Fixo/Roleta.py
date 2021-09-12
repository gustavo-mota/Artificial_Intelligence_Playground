import random

'''
01. var pesos[10]:int = {1,1,1,1,2,3,4,5,5,5};
02  var somaPeso:int = 0;
03. PARA var i=0 ATE 9 FAÇA
04.   somaPeso+=pesos[i];
05. FIMPARA
06. var sorteio:INT = ALEATORIO(0,somaPeso);
07. var posicaoEscolhida = -1;
08. FAÇA:
09.    posicaoEscolhida++;
10.    somaPeso -= pesos[posicaoEscolhida];
11. ENQUANTO(somaPeso>0);
'''

'''
pesos = [1,1,1,1,1,1,1,1,1,1]
#pesos = [1, 1, 1, 1, 2, 3, 4, 5, 5, 5] # cada posição corresponde a uma pergunta
somaPesos = sum(pesos)
sorteio = random.randint(0, somaPesos)
posicaoEscolhida = -1
while sorteio > 0:
    posicaoEscolhida += 1
    sorteio -= pesos[posicaoEscolhida]
print(pesos[posicaoEscolhida], ", ", posicaoEscolhida)

print(len(pesos))'''

def Roleta(vetor):
    somaPesos = sum(vetor)
    # Before. try with somaPesos converted to int
    sorteio = random.uniform(0, somaPesos)  # Error randint don't works with floats
    posicaoEscolhida = -1
    while sorteio > 0:
        posicaoEscolhida += 1
        sorteio -= vetor[posicaoEscolhida]

    return posicaoEscolhida

# choices(lista, weight=None, cum_weight=None, k=1)[0]