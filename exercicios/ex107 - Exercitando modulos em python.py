from exercicios import moedas

#Programa principal
p = float(input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moedas.metade(p)}')
print(f'o dobro de R${p} é R${moedas.dobro(p)}')
print(f'aumentando 10% temos R${moedas.aumentar(p)}')
print(f'Reduzindo 13% temos R${moedas.diminuir(p)}')

