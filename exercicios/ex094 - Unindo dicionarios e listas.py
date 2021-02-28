pessoa = {}
lista = []
cont = media = 0
totidade = 0

mc = []
mediaidade = []
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        print('ERRO! por favor, digite apesa M ou F')
        pessoa['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))

    if pessoa['sexo'] == 'F':
        mc.append(pessoa['nome'])
    totidade += pessoa['idade']
    lista.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')


    if resp == 'N':
        break

print('=-' * 30)

print(f'Ao todo temos {len(lista)} pessoas cadastradas')
media = totidade / len(lista)
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram ', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'[{p["nome"]}]', end='')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f' {k} = {v}  ', end='')
        print()
print('<< Encerrado >>')

