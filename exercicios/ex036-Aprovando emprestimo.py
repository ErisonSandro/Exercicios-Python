#APROVANDO EMPRESTIMO

casa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))

meses = anos * 12
prestação = casa / meses

print('Para pagar uma casa de R${:.2f} em {} anos a prestação sera de R${:.2f}'.format(casa, anos, prestação))

if prestação >= salario * 30 /100:
    print('Emprestimo negado')

else:
    print('Emprestimo pode ser CONCEDIDO!')

