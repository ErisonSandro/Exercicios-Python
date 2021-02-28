c = str(input('Digite o nome de uma cidade: ')).upper()

div = c.split()
jun = div[0]

print('Sua cidade tem santo no nome: {} '.format('SANTO' in jun))

