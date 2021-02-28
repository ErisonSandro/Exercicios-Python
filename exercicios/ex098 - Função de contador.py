from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    print('=-' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')



    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont += passo
        print('Fim')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.3)
            cont -= passo
        print('fim')


contador(1, 10, 1)
contador(10, 1, 2)

print('Agora é a sua vez!')
ini = int(input('Inicio: '))
fi = int(input('Fim '))
pas = int(input('Passo: '))
contador(ini, fi, pas)
