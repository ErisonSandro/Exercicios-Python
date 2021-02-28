while True:
    num = int(input('Quer ver a tabuada de qual valor: '))
    print('-=' * 20)
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{num}x{cont} = {num * cont}')
    print('-=' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')


print('-='*20)