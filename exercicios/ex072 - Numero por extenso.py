num20 = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
numero = 0
while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero > 20 or numero < 0:
        print('Tente Novamente. ', end='')
    else:
        break
print(f'Voce digitou o numero {num20[numero]}')
