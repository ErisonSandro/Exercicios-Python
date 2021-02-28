print('=' * 10, 'Loja Nene', '=' * 10)
preço = float(input('Preço das compras: R$ '))

print('Forma de pagamento:')
print('[1] à vista dinheiro / cheque')
print('[2] à vista no cartão')
print('[3] 2x no cartão de credito')
print('[4] 3x ou mais no cartão de credito')

opção = int(input('Qual é a sua opção: '))

if opção == 1:
    d1 = preço - (preço*10/100)
    print('Sua compra de R${} vai custar R${} no final'.format(preço, d1))
elif opção == 2:
    d2 = preço - (preço*5/100)
    print('Sua compra de R${} vai custar R${} no final'.format(preço, d2))
elif opção == 3:
    parcela = int(input('Quantas parcelas: '))
    print('Sua compra sera em {}x de {} sem juros!'.format(preço, preço / parcela))
    print('Sua compra vai custar R${}'.format(preço))

elif opção == 4:
    parcelas = int(input('Quantas parcelas: '))
    j1 = preço + (preço*20/100)
    juros = j1 / parcelas
    print('Sua compra sera parcelada em {}x de {} com juros'.format(parcelas, juros))
    print('Sua compra foi de R${} vai custar R${} parcelando em 3x'.format(preço, j1))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')