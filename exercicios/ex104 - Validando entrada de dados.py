def leiaint(txt):
    valor = input(txt)
    if valor.isnumeric():
        return valor
    else:
        print('\033[1;31mErro!, Digite um numero inteiro!\033[m')
    return leiaint(txt)

n = leiaint('Digite um numero: ')
print(f'Voce digitou {n}')
