somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for pessoa in range(1, 5):
    print('----{}ª Pessoa-----'.format(pessoa))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    médiaidade = somaidade / 4
    if pessoa == 1 and sexo in 'mM':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if idade < 20 and sexo in 'Ff':
        totmulher20 += 1



print('A média de idade do grupo é de {} anos'.format(médiaidade))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('No grupo tem {} mulheres menores de 20 anos'.format(totmulher20))

