nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = (nota1 + nota2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(nota1, nota2, media))
if media < 5.0:
    print('O aluno esta REPROVADO')
elif media >= 5 and media < 6.9:
    print('O aluno esta de RECUPERAÇÃO')
else:
    print('O aluno foi APROVADO')
