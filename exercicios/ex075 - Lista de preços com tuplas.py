cont = par = 0

valores = (int(input('Digite um numero: ')),
    int(input('Digite outro numero: ')),
    int(input('Digite mais um numero: ')),
     int(input('Digite o ultimo numero: ')))

print(f'Você digitou os valores {valores}')

print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor valor 3 aparece na {valores.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado! ')
print('Os valores pares digitados foram ', end='')

for n in valores:
    if n % 2 == 0:
        print(n, end=' ')
