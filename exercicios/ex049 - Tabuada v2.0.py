from time import sleep
num = int(input('Digite um numero para ver sua tabuaba: '))

for cont in range(1, 11):
    soma = num * cont
    sleep(0.3)
    print('{}x{} = {}'.format(num, cont, soma))
