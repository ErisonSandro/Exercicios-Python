def numero(* num):
    maior = 0
    cont = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    for valor in num:
        print(f'{valor}', end=' ')


        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f' Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')


numero(2, 9, 4, 5, 7, 1)
numero(4, 7, 0)
numero(1, 2)
numero(6)
numero()

