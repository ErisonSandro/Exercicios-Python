from random import randint
from  time import sleep


valores = [randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5), randint(0, 5)]
def sorteio(lst):
    print('Sorteando 5 numeros da lista:', end=' ')
    for l in lst:
        print(l, end=' ')
        sleep(0.5)
    print('pronto')


sorteio(valores)
def somapar(lista):
    soma = 0
    si = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
        else:
            si += valor

    print(f'Somando os valores pares de {lista}, temos {soma}')
    print(f'Somando os valores impares de {lista}, temos {si}')

somapar(valores)



