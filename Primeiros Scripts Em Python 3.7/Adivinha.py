from time import sleep

from random import randint

nome = str(input("Digite seu nome: "))

print ("")

print('-=-' * 20)

print('Pensando em um numero entre 0,5 !')

print('-=-' * 20)

print ("")

computar = randint(0, 5)

jogador = int(input("Digite um numero entre 0, 5: "))

print ("")

print('PROCESSANDO...')

print ("")

sleep(3)

if(computar == jogador):

    print("{}, você ganhou Parabens!".format(nome))

else:

    print("{}, você perdeu!, o computador digitou {} e você {}".format(nome, computar, jogador))