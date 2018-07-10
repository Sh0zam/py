conta = 0

contador = int(0)
while True:

    contador += 1
    nota = float(input("Digite Suas Nota Para parar digite: "))

    print("")

    verificar = str(input("Quer continuar [S/N]")).upper().strip()[0]

    print("")

    conta += nota

    if verificar == "N":
        break

seila = conta / contador

print("Sua media desse Bimestre foi: {:.2f}".format(seila))
