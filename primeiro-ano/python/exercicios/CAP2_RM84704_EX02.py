'''
Sua tarefa é criar um algoritmo que receba o tipo de assinatura 
do cliente e o faturamento anual dele e calcule e exiba qual o 
valor do bônus que o cliente deve pagar a vocês. A tabela abaixo 
mostra a porcentagem de acordo com cada nível de assinaturas:
'''


print(" ---------------------")
print("| VALOR BONUS A PAGAR |")
print(" ---------------------")

print(" --------------------------------------------------- ")
print("| 1 - Basic | 2 - Silver | 3 - Gold | 4 - Platinum  |")
print(" --------------------------------------------------- ")

try:
	
	assinatura = int(input("Qual o numero correspondente a sua assinatura: "))
	valor_faturamento = float(input("Insira o valor do faturamento (Reais): "))

	if assinatura ==1:
	    print("Bonus a pagar: {:.2f}".format(valor_faturamento * 0.3))
	elif assinatura ==2:
	    print("Bonus a pagar: {:.2f}".format(valor_faturamento * 0.2))
	elif assinatura ==3:
	    print("Bonus a pagar: {:.2f}".format(valor_faturamento * 0.1))
	elif assinatura ==4:
	    print("Bonus a pagar: {:.2f}".format(valor_faturamento * 0.05))
	else:
	    print("Insira novamente o numero correspondente.")

except ValueError:
	  print("Oops! valor invalido. Tente novamente...")
