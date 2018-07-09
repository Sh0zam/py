from random import randint

from time import sleep

nome = str(input('Digite seu nome: ')).strip()
print('''Você tem 3 opções para escolher!:
<1> Pedra
<2> Papel
<3> Tesoura''')

jogador = int(input("Qual a sua jogada?: "))

print("\033[1;36mJO\033[m")
sleep(1)
print("\033[1;37mKEN\033[m")
sleep(1)
print("\033[1;34mPOOO!!!!\033[m")

print('')

jogo = ["Pedra", "Papel", "Tesoura"]

computar = randint (1, 3)

if computar == 1:

    if jogador == 1:


        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print ('Você empatou com o computador ')

    elif jogador == 2:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print ('Você ganhou parabens!')

    elif jogador == 3:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print('Você perdeu !')

    
    else:

        print("Opção invalida!")

       

elif computar == 2:

    if jogador == 1:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Você perdeu !")


    elif jogador == 2:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Você empatou com o computador!")

    elif jogador == 3:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Parabens você ganhou!")

    else:

        print("Opção invalida!")
    
elif computar == 3:

    if jogador == 1:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Parabens você ganhou")

    elif jogador == 2:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Você perdeu")

    elif jogador == 3:

        print('-=-' * 12)

        print('O Computador jogou {}'.format(computar))

        print("E o {} jogou {}".format(nome, jogador))

        print('-=-' * 12)

        print("Você empatou com o computador")

    else:

        print("Opção invalida!")

else:
    print("Opção invalida!")
