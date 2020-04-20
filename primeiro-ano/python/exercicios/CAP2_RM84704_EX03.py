'''
Os alunos da sua turma fizeram uma votação para escolher qual
dia da semana é o melhor para a realização das lives. Faça um 
programa em que o usuário informe a quantidade de votos que 
cada um dos 5 dias (segunda-feira, terça-feira, quarta-feira,
quinta-feira e sexta-feira) obtiveram, verifique e exiba qual
dia venceu.
'''



print(" -------------------")
print("| VOTAÇÃO LIVE FIAP |")
print(" -------------------")

print("insira o valor de votos de cada dia: ")

try:

	segunda_feira = int(input("Segunda-feira: "))
	terca_feira = int(input("Terça-Feira: "))
	quarta_feira = int(input("Quarta-Feira: "))
	quinta_feira = int(input("Quinta-Feira: "))
	sexta_feira = int(input("Sexta-Feira: "))
	
	if segunda_feira > terca_feira and segunda_feira > quarta_feira and segunda_feira > quinta_feira and segunda_feira > sexta_feira:
    		print("O dia com mais votos foi Segunda-Feira com {} votos.".format(segunda_feira))

	elif terca_feira > segunda_feira and terca_feira > quarta_feira and terca_feira > quinta_feira and terca_feira > sexta_feira:
    		print("O dia com mais votos foi Terça-Feira com {} votos.".format(terca_feira))

	elif quarta_feira > segunda_feira and quarta_feira > terca_feira and quarta_feira > quinta_feira and quarta_feira > sexta_feira:
    		print("O dia com mais votos foi Quarta-Feira com {} votos.".format(quarta_feira))

	elif quinta_feira > segunda_feira and quinta_feira > terca_feira and quinta_feira > quarta_feira and quinta_feira > sexta_feira:
    		print("O dia com mais votos foi Quinta-Feira com {} votos.".format(quinta_feira))

	elif sexta_feira > segunda_feira and sexta_feira > terca_feira and sexta_feira > quarta_feira and sexta_feira > quinta_feira:
    		print("O dia com mais votos foi Sexta-Feira com {} votos.". format(sexta_feira))

except ValueError:
	print("Oops! valor invalido. Tente novamente...")



