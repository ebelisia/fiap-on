'''
1 – O projeto HealthTrack é o máximo e tem grande possibilidade
de impactar positivamente a vida das pessoas. Mesmo que a solução
final não utilize uma implementação em Python, podemos aproveitar 
a oportunidade para desenvolver o algoritmo que resolva um problema 
simples: o cálculo do IMC sem distinção de sexo biológico. Por isso, 
você deve desenvolver um script que solicite o PESO e a ALTURA de uma 
pessoa. A partir disso, o script deva calcular o IMC (PESO dividido 
pelo quadrado da ALTURA) e informar em que faixa a pessoa se encontra, 
de acordo com a divisão a seguir:
'''


print(" ------------- ")
print("| Cálculo IMC |")
print(" ------------- ")

try:
	peso = float(input("Insira o seu peso: "))
	altura = float(input("Insira a sua altura (exemplo: 1.65): "))

	imc = (peso / (altura * altura))
	print ("O IMC é: {:.2f}".format(imc))

	if (imc < 16):
	    print("Categoria: Baixo peso Grau 3.")

	elif (imc <= 16.99):
	    print("Categoria: Baixo peso grau 2.")

	elif (imc <= 18.49):
	    print("Categoria: Baixo peso grau 1.")

	elif (imc <= 24.99):
	    print("Categoria: Peso ideal.")

	elif (imc <= 29.99):
	    print("Categoria: Sobre peso.")

	elif (imc <= 34.99):
	    print("Categoria: Obesidade grau 1")

	elif (imc <= 39.99):
	    print("Categoria: Obesidade grau 2")

	else:
	    print("Categoria: Obesidade grau 2")

except ValueError:
	  print("Oops! valor invalido. Tente novamente...")



