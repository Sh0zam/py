conta = 0
contador = int(0)

while True:

    nota = float(input("Digite Suas Notas: "))
    conta += nota
    contador += 1

    if nota > 10.00:
        print("Sua nota é invalida Iremos recomeçar tudo ! Zeramos todas as notas que você colocou!")
        nota = 0
        conta = 0
        contador = 0

    if contador >= 3:
        verificar = str(input("Quer continuar [S/N]: ")).upper().strip()[0]
        if verificar == "N":
            break

seila = conta / contador
print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")
print("| Sua media desse Bimestre foi: {:.2f}  |".format(seila))
print("|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|")                   
