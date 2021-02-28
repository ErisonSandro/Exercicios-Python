peso = float(input('Qual é o seu peso (kg): '))
altura = float(input('Qual é a sua altura (m): '))

imc = peso / (altura ** 2)

print('O IMC da pessoa é {:.1f}'.format(imc))

if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc <= 25:
    print('Parabens voce esta no PESO IDEIAL')
elif imc <= 30:
    print('voce esta SOBREPESO, precisa emagrecer!')
elif imc <= 40:
    print('voce esta em OBESIDADE, precisa emagrecer urgente')
else:
    print('voce esta em OBESIDADE MÓRBIDA, cuidado!')



