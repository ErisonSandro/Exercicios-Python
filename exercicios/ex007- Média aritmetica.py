#desenvolva um programa que leia as duas notas de um aluno,
#calcule e mostre a sua média

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
total = nota1 + nota2
media = total / 2

print('sua primeira nota é {} segunda nota {} e a média é {:.1f}'.format(nota1, nota2, media))



