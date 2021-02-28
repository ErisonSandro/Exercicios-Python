#Crie um programa que leia quanto dinheiro uma pessoa tem na
# sua carteira e mostre quandos dolares ela pode comprar (considere US1,00=3,27)

carteira = float(input('Quanto dinheiro voce tem na carteira? R$'))
dolar = carteira / 5.19

print('Com R${} voce pode comprar U${:.2f}'.format(carteira, dolar))


