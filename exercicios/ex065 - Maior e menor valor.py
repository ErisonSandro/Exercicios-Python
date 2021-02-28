cont = 0
media = 0
soma = 0
maior = 0
menor = 0

numero = 0
continuar = 0

while continuar != 'N':
    numero = int(input('Digite um numero: '))

    cont += 1
    soma += numero
    media = soma / cont
    if cont == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    continuar = str(input('Quer continuar [S/N] : ')).upper().strip()[0]
print('Voce digitou {} numeros e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
