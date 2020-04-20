'''
Por essa razão, você deve elaborar um algoritmo implementado
em Python em que o usuário informe quantos alimentos consumiu
naquele dia e depois possa informar o número de calorias de
cada um dos alimentos. Como não estudamos listas nesse
capítulo você não deve se preocupar em armazenar todas as
calorias digitadas, mas deve exibir o total de calorias no final.
'''

total = 0
count = 1
qntAlimento = int(input('Digite a quantidade de alimentos ingeridos hoje: '))
for x in range(qntAlimento):
    count = int(count + 1)
    total += int(input("Insira a quantidade de calorias do alimento %s:"%(count-1)))
print("Total de calorias consumidas hoje: %s"%total)


