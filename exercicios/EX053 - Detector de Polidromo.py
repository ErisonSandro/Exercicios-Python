frase = str(input('Digite uma frase: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('o inverso de {} é {}'.format(junto, inverso))

if inverso == junto:
    print('É POLINDROMO')
else:
    print('NÃO É POLINDROMO')

