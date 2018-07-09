from time import sleep

import os

def Fim():
    os.system('cls' if os.name == 'clear' else 'clear')

    print("Obrigado por usar meu Script!")

    print("")

    print("Version 3.0.1!")

    print("")

    print("Caso encontre algum erro ou mal funcionamento entre em contanto \"Shazam #6231\"")

    print("")

    print("Create BY: Shazam!,\"www.github.com/sh0zam/py\"")

    print("")

    print("SAINDO...")

    sleep(5)

    print("")

    print("LIMPANDO CONSOLE!")

    sleep(3)

    os.system('cls' if os.name == 'clear' else 'clear')

    exit()

#caixa de encontrar raiz
def potencia(x, y):

    return x ** (1/2)

##Caixa de adicacao
def add(x, y):

    return x + y

#Caixa de subtracao
def sub(x, y):

    return x - y

#Caixa de mutiplicacao
def multi(x, y):

   return x * y

#Caixa de divisao
def div(x, y):

   return x / y

#caixa de raiz
def raizk(x,y):

    return x * x

while True:

    os.system('cls' if os.name == 'clear' else 'clear')

    print("Selecione Sua Operação abaixo!:")

    print("1.Adição")

    print("2.Subtração")

    print("3.Mutiplicacão")

    print("4.Divisão")

    print("5.Descobrir a raiz quadrada de um numero")

    print("6.Calcular uma raiz Ex: 2²")

    print("7.Surpresa! :c")

    print("")

    escolha = int(input("Faça sua escolha(1,2,3,4,5,6,7 ou 10 para sair!): "))

    print("")
        
    if escolha == 10:

        Fim()


    elif escolha == 1:

        num = float(input("Digite o primeiro Numero: "))

        print("")

        numm = float(input("Digite outro Numero!: "))

        print("")

        print('-=--=--=--=--=--=--=--=-')

        print(num,"+",numm, "=", add(num,numm))

        print('-=--=--=--=--=--=--=--=-')

        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del num,numm

    elif escolha == 2:

        num = float(input("Digite o primeiro Numero: "))

        print("")

        numm = float(input("Digite outro Numero!: "))

        print("")

        print('-=--=--=--=--=--=--=--=-')

        print(num,"-",numm, "=", sub(num,numm))

        print('-=--=--=--=--=--=--=--=-')

        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del num,numm

    elif escolha == 3:

        num = float(input("Digite o primeiro Numero: "))

        print("")

        numm = float(input("Digite outro Numero!: "))

        print("")

        print('-=--=--=--=--=--=--=--=-')

        print(num,"*",numm,"=", multi(num,numm))

        print('-=--=--=--=--=--=--=--=-')

        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del num,numm

    elif escolha == 4:

        num = float(input("Digite o primeiro Numero: "))

        print("")

        numm = float(input("Digite outro Numero!: "))

        print("")

        print('-=--=--=--=--=--=--=--=-')

        print(num,"/",numm,"=", div(num,numm))

        print('-=--=--=--=--=--=--=--=-')

        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del num,numm

    elif escolha == 5:

        raiz = float(input("Digite o numero: "))

        print('-=--=--=--=--=--=--=--=-')

        print("A raiz quadrada de {} é :".format(raiz), potencia(raiz,raiz))

        print('-=--=--=--=--=--=--=--=-')
        
        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del raiz

    elif escolha == 6:

        rai = float(input("Digite o numero: "))

        print('-=--=--=--=--=--=--=--=-')

        print("Sua resposta é:",raizk(rai,rai),"²")

        print("-=--=--=--=--=--=--=--=-")

        print("5 SEGUNDOS ANTES QUE LIMPE O CONSOLE!")

        sleep(5)

        del rai

    elif escolha == 7:

        print('''
                       .
                       M
                      dM
                      MMr
                     4MMML                  .
                     MMMMM.                xf
     .              "MMMMM               .MM-
      Mh..          +MMMMMM            .MMMM
      .MMM.         .MMMMML.          MMMMMh
       )MMMh.        MMMMMM         MMMMMMM
        3MMMMx.     'MMMMMMf      xnMMMMMM"
        '*MMMMM      MMMMMM.     nMMMMMMP"
          *MMMMMx    "MMMMM\    .MMMMMMM=
           *MMMMMh   "MMMMM"   JMMMMMMP
             MMMMMM   3MMMM.  dMMMMMM            .
              MMMMMM  "MMMM  .MMMMM(        .nnMP"
  =..          *MMMMx  MMM"  dMMMM"    .nnMMMMM*
    "MMn...     'MMMMr 'MM   MMM"   .nMMMMMMM*"
     "4MMMMnn..   *MMM  MM  MMP"  .dMMMMMMM""
       ^MMMMMMMMx.  *ML "M .M*  .MMMMMM**"
          *PMMMMMMhn. *x > M  .MMMM**""
             ""**MMMMhx/.h/ .=*"
                      .3P"%....
                    nP"     "*MMnx                
''')
        print("Eita porra :C")


        sleep(10)

        
        print("")

    else:
        
        print("Operação Não encontrada para não ocorrer bugs iremos sair do programa em 3 segundos")

        sleep(3)

        exit()
