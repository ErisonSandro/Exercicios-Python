
escola = {}

escola['nome'] = str(input('Nome: '))
escola['media'] = float(input(f'Média de {escola["nome"]}: '))


if escola['media'] >= 7:
    escola['Situação'] = 'Aprovado'
elif 5 <= escola['media'] < 7:
    escola['Situação'] = 'Recuperação'
else:
    escola['Situação'] = 'Reprovado'

for k, i in escola.items():
        print(f'{k} é igual a {i}')


