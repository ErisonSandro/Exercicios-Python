cont = 0
numero = 0
soma = 0
numero = int(input('Digite um numero [999 para parar]: '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite um numero [999 para parar]: '))
print('Voce digitou {} numeros e a soma entre eles foi {} '.format(cont, soma))