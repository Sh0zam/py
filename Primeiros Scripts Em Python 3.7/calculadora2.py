from time import sleep

from datetime import date
##-------------------------------##
def Fim():
    print("Obrigado por usar meu Script!")

    print("")

    print("Version 2.0.1!")

    print("")

    print("Caso encontre algum erro ou mal funcionamento entre em contanto \"Shazam #6231\"")

    print("")

    print("Create BY: Shazam!,\"www.github.com/sh0zam/py\"")

    print("")

    print("SAINDO...")

    sleep(3)

    exit()
##-----Bloco Acima é o bloco Fim##

##-----Bloco abaixo é o bloco Principal##
def Principal():
    while True:

        xy = str(input("Caso queira sair digite \"q\" or \"Q\": "))

        if xy == "q" or xy == "Q":

            Fim(); 

        x = int(input("Digite o primeiro numero !: "))

        print("")

        operacao = str(input("Digite a operação que ira usar!: "))

        print("")

        y = float(input("Digite o segundo numero!: "))


        if operacao == "+":

            print("CALCULANDO.")
            
            sleep(0.8)

            print("CALCULANDO..")
            
            sleep(0.8)

            print("CALCULANDO...")
            
            sleep(0.8)

            print('')

            resultado = x + y

            print("Seu resultado é: {:.2f}".format(resultado))

            print("")
    
        elif operacao == "-":

            print("CALCULANDO.")
            
            sleep(0.8)

            print("CALCULANDO..")
            
            sleep(0.8)

            print("CALCULANDO...")
            
            sleep(0.8)

            print('')

            resulfado = x - y

            print("Seu resultado é: {:.2f}".format(resulfado))

            print("")
    
        elif operacao == "*":

            print("CALCULANDO.")
            
            sleep(0.8)

            print("CALCULANDO..")
            
            sleep(0.8)

            print("CALCULANDO...")
            
            sleep(0.8)

            print("")

            resultaho = x * y

            print("Seu resultado é: {:.2f}".format(resultaho))

            print("")

        elif operacao == "/":

            print("CALCULANDO.")
            
            sleep(0.8)

            print("CALCULANDO..")
            
            sleep(0.8)

            print("CALCULANDO...")
            
            sleep(0.8)

            print("")

            resultados = x / y

            print("Seu resultado é: {:.2f}".format(resultados))

            print("")

        else:

            print("ERROR404")

            print("Operação invalida.")
            
            sleep(1.5)

            print("ERROR404")

            print("Operação invalida!")
            
            sleep(1.5)

            print("ERROR404")
            
            sleep(1.8)

            print("")

            print("Algo deu errado")

            print("")
            
            print("Para o Sistema não bugar estamos entrando em modo defesa, estamos saindo!")

            sleep(3.5)

            print("")

            Fim()


Principal();

