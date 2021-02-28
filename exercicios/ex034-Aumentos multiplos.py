salario = float(input('Qual é o salario do funcionario? R$'))

a1 = salario + (salario * 10 / 100)
a2 = salario + (salario * 15 / 100)


if salario > 1250:
    print('Quem ganhava {:.2f} passa a ganhar {:.2f}'.format(salario, a1))

if salario <= 1250:
    print('Quem ganhava {:.2f} passa a ganhar {:.2f}'.format(salario, a2))

