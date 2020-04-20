'''
Muitos professores preferem adotar modelos diferentes de provas
quando dão aulas para turmas muito grandes. Por essa razão, a 
escola de inglês JoWell Sant’ana, em que todas as turmas são compostas
por 50 alunos, solicitou que você criasse um sistema capaz de atender
ao seguinte requisito: o professor deve digitar primeiro as notas dos 25 
alunos que tem número ímpar na chamada (1, 3, 5, ..., 47, 49) e depois as 
notas dos 25 alunos que tem número par (2, 4, 6,..., 48, 50). O sistema 
deve calcular e exibir a média de cada uma das metades da sala e informar,
ao final, qual delas teve a maior nota.

Há ainda um pedido especial do mantenedor: para que os professores não se confundam,
ao digitar cada uma das notas deve ser exibida uma mensagem no seguinte padrão:

VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES (ou ímpares, quando for o caso).

POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO x.
'''



numeroAlunos = 50
x = 1
total_impar = 0
total_par = 0
for x in range(numeroAlunos):
    if x % 2 == 0:
        total_impar += float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES. (ALUNO %s): "%(x+1)))

for x in range(numeroAlunos):
    if x % 2 == 1:
        total_par += float(input("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES. (ALUNO %s): "%(x+1)))

mediaImpar = total_impar/25 
mediaPar = total_par/25 

print("A MÉDIA DOS ALUNOS ÍMPARES É: %s"%(mediaImpar))
print("A MÉDIA DOS ALUNOS PARES É: %s"%(mediaPar))

if mediaImpar > mediaPar:
    print("SENDO ASSIM, A MÉDIA DAS NOTAS DOS ALUNOS ÍMPARES É MAIOR.")
else:
    print("SENDO ASSIM, A MÉDIA DAS NOTAS DOS ALUNOS PARES É MAIOR.")

    