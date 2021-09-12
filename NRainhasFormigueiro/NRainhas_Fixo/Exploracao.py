import threading
import time
from FormigasSolucao import *
from FormigasFeromonio import *
from FormigasFixo import *

def Exploracao(iteracao, evaporacao, formigueiro, modo):
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

    elif modo == 4:
        # modo direto
        i = 0
        whileVar = 1
        formiga = -1
        teste = -1

        formigueiro.formigueiro[0].__run__(feromonio)
        print(formigueiro.formigueiro[0].caminho)
        '''
        while (True):
            S = threading.Semaphore(formigueiro.k)
            for f in range(formigueiro.k):
                # Still needing tests
                # It can need try and exception
                S.acquire()
                formigueiro.formigueiro[f].start()
                #time.sleep(1)
                print("aqui ", f)
                #formigueiro.formigueiro[f].join()
                #time.sleep(0.001)

                if teste == 1:
                    print("Solução em potencial encontrada, Exploração\n")
                    formiga = f
                    whileVar = 0
                    break
            S.release()
            if whileVar == 0:
                break
            feromonio.__atualizacao__(formigueiro)
            print("Iteração ", i, "terminada\n")
            i += 1
        print("Solução achada pela formiga ", formiga)
        FormigasSolucao(formigueiro.formigueiro[formiga].caminho)
        '''
    elif modo ==5:
        Feromonio = FormigasFeromonio(evaporacao)
        # Criar formigas
        Formiga00 = Formiga(0)
        Formiga01 = Formiga(1)
        Formiga02 = Formiga(2)
        Formiga03 = Formiga(3)
        Formiga04 = Formiga(4)
        Formiga05 = Formiga(5)
        Formiga06 = Formiga(6)
        Formiga07 = Formiga(7)

        Formiga08 = Formiga(8)
        Formiga09 = Formiga(9)
        Formiga10 = Formiga(10)
        Formiga11 = Formiga(11)
        Formiga12 = Formiga(12)
        Formiga13 = Formiga(13)
        Formiga14 = Formiga(14)
        Formiga15 = Formiga(15)

        Formiga16 = Formiga(16)
        Formiga17 = Formiga(17)
        Formiga18 = Formiga(18)
        Formiga19 = Formiga(19)
        Formiga20 = Formiga(20)
        Formiga21 = Formiga(21)
        Formiga22 = Formiga(22)
        Formiga23 = Formiga(23)

        Formiga24 = Formiga(24)
        Formiga25 = Formiga(25)
        Formiga26 = Formiga(26)
        Formiga27 = Formiga(27)
        Formiga28 = Formiga(28)
        Formiga29 = Formiga(29)
        Formiga30 = Formiga(30)
        Formiga31 = Formiga(31)

        Formiga32 = Formiga(32)
        Formiga33 = Formiga(33)
        Formiga34 = Formiga(34)
        Formiga35 = Formiga(35)
        Formiga36 = Formiga(36)
        Formiga37 = Formiga(37)
        Formiga38 = Formiga(38)
        Formiga39 = Formiga(39)
        # Criação de formigas terminada
        while True:
            feromonioDeposito = copy.deepcopy(Feromonio)
            # Decisão e atualização
            try:
                feromonioDeposito.__deposito__(Formiga00.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga01.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga02.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga03.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga04.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga05.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga06.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga07.__decisao__(Feromonio))

                feromonioDeposito.__deposito__(Formiga08.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga09.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga10.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga11.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga12.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga13.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga14.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga15.__decisao__(Feromonio))

                feromonioDeposito.__deposito__(Formiga16.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga17.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga18.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga19.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga20.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga21.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga22.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga23.__decisao__(Feromonio))

                feromonioDeposito.__deposito__(Formiga24.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga25.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga26.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga27.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga28.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga29.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga30.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga31.__decisao__(Feromonio))

                feromonioDeposito.__deposito__(Formiga32.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga33.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga34.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga35.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga36.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga37.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga38.__decisao__(Feromonio))
                feromonioDeposito.__deposito__(Formiga39.__decisao__(Feromonio))
            except:
                break
            # Decisão e atualização fim
            Feromonio = copy.deepcopy(feromonioDeposito)
            Feromonio.__evaporacao__()
    else:
        print("Tente uma opção válida")
