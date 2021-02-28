#faça um algoritmo que leia o salario de um funcionario e mostre seu novo
# salario com 15% de aumento!


salario = float(input('Qual é o salario do funcionario? R$'))
aumento = salario + (salario*15/100)


print('o salario de {:.2f} com aumento de 15% fica R${:.2f} '.format(salario, aumento))

