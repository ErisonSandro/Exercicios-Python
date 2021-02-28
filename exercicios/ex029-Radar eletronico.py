vel = float(input('Qual é a velocidade atual do carro? '))

multa = float(vel - 80) * 7
print('')
if vel > 80:
    print('MULTADO! você excedeu o limite permitido que é de 80Km/h')
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')