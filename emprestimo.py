from time import sleep

casa = float(input('Digite o valor da Casa!: R$ '))

print('')

salario = float(input('Digite quanto por Mês você ganha!: '))

print("")

anos = int(input('Em quantos anos deseja parcelar?: '))

print('')

minimo = salario * 30 /100

prestacao = casa / (anos * 12)

print("PROCESSANDO.")
sleep(1.5)
print("PROCESSANDO..")
sleep(1.6)
print("PROCESSANDO...")
sleep(1.7)

print("")
print("Para você pagar uma Casa de R${:.2f} em \"{}\" anos.".format(casa, anos))
print("A prestação sera de R${:.2f}.".format(prestacao))
print("\"30%\" do seu salario de \"{}\" é \"{}\".".format(salario, minimo))
print("")

if prestacao <= minimo:
    print("EMPRESTIMO concedido!")
    print("Você com \"30%\"do seu salario consegue pagar o EMPRESTIMO!")

else:
    print("EMPRESTIMO negado!")
    print("Você com \"30%\" do seu salario não consegue pagar o EMPRESTIMO!")
