import random

a1 = str(input('primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
sorteio = random.choice(alunos)

print('o aluno escolhido foi {}'.format(sorteio))
