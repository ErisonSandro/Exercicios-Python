from datetime import date
anoatual = date.today().year


cadastro = {}

cadastro['nome'] = str(input('Nome:'))
cadastro['idade'] = anoatual - int(input('Ano de nascimento: '))
idade = anoatual - cadastro['idade']
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de contratação: '))
    cadastro['salario'] = float(input('Salario: '))
    tempotrab = anoatual - cadastro['contratação']
    cadastro['Aposentadoria'] = (35 - tempotrab) + cadastro['idade']

print('=-' * 10)
for c, v in cadastro.items():
    print(f'    - {c} tem o valor {v}')




