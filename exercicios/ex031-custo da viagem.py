distancia = float(input('Qual é a distancia da viagem? '))
print('Voce esta prestes a começar uma viagem de {:.2f}Km'.format(distancia))

if distancia <= 200:
    preço = distancia * 0.50
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))
else:
    preço = distancia * 0.45
    print('E o preço da sua passagem será de R${:.2f}'.format(preço))