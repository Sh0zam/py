##Meu primeiro Codigo de python 
##By:Shazam
##Calculadora de todas as operações 
def menu():
	 x = float(input("Primeiro Numero: "));

	 
	 print("")
	 
	 operacao = input("Operação: ");


	 print("")

	 y = float(input("Segundo Numero: "));


	 print("")

	
	 if operacao == "+":


		 print("Seu Resultado é:", x + y)


		 print("")


	 elif operacao == "-":


		 print("Seu Resultado é:", x - y)


		 print("")


	 elif operacao == "*":


		 print ("Seu Resultado é:", x * y)


		 print("")


	 elif operacao == "/":


		 print(" Seu resultado é:", x / y )


		 print("")


	 else:


		 print('A operação é invalida')


		 print("")

     
     

	 print ("Codigo BY:Shazam");


	 print("");


	 print("");


	 x = int(input("""Você quer voltar para o menu digite: 0
Se você não quer continuar usando aperte qualquer numero: """));


	 print("");


	 print("");


	 if x == 0:
	 	menu()


	 else:
	    print("Obrigado por usar meu programa !");


menu();

##Use e melhore esse codigo 
##Qualquer um pode usar !


    
