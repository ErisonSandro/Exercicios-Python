nome = str(input('Digite seu nome completo: ')).lower()

div = nome.split()
silva = 'silva' in div


print('Voce tem silva no nome: {} '.format(silva))