def menu():

	x = float(input("Digite a Primeira nota do aluno: "))

	z = float(input("Digite a Segunda nota do aluno: "))

	y = float(input("Digite a Terceira nota do aluno: "))
 
	v = float(input("Digite a Quarta nota do aluno: "))

	print("")

	média = (x + z + y + v) / 4

	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

	print("   A média entre a Primeira nota: {:.1f}, Segunda Nota: {:.1f}".format(x, z))

	print("   Terceita Nota: {:.1f}, e Quarta Nota: {:.1f}".format(y, v))

	print("   A média final é:",média)

	print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

	print("")

	con = int(input("""Se você quer refazer sua conta digite: 0,
caso não queria digite qualquer numero """));
   
	print("")

	if(con == 0):

         print("")

         menu();

	else:

		print("")

		print("Codigo BY: Shazam!")

		print("")

		print("https://github.com/Sh0zam/py")

		print("");

menu()		

 	

