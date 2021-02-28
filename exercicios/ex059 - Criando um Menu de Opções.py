from time import sleep
maior = 0

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NUMEROS \n[5] SAIR DO PROGRAMA')
opçao = int(input('Qual é a sua opção? '))

while opçao != 5:
    if opçao == 1:
        soma = primeiro + segundo
        print('A soma entre {} + {} é {}'.format(primeiro, segundo, soma))

    elif opçao == 2:
        mult = primeiro * segundo
        print('O resultado de {}x{} = {}'.format(primeiro, segundo, mult))

    elif opçao == 3:
        if primeiro > segundo:
            maior = primeiro
        else:
            maior = segundo
        print('O maior numero digitado é {}'.format(maior))

    elif opçao == 4:
        print('Informe os numeros novamente: ')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
    else:
        print('Numero invalido, Tente novamente')
    sleep(2)
    print('=-'*10)
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR \n[4] NOVOS NUMEROS \n[5] SAIR DO PROGRAMA')
    opçao = int(input('Qual é a sua opção? '))
