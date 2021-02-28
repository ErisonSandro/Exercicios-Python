totidade = homens = mulheresmenores = 0

while True:
    print('-'*20)
    print('Cadastre uma pessoa')
    print('-'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    cont = ' '
    while cont not in 'SN':
        cont = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if cont == 'S':
        if idade > 18:
            totidade += 1
        if sexo == 'M':
            homens += 1
        if sexo == 'F' and idade < 20:
            mulheresmenores += 1


    else:
        print(f'Total de pessoas com mais de 18 anos: {totidade}')
        print(f'Ao todo temos {homens} homens cadastrados')
        print(f'E temos {mulheresmenores} mulheres com menos de 20 anos!')
        break


