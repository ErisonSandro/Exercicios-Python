from datetime import date


ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - ano
alista = ano + 18



print('Quem nasceu hein {} tem anos {} em {}'.format(ano, idade, atual))

if idade == 18:
    print('Voce tem que se alistar IMEDIATAMENTE')
elif idade > 18:
    print('Voce ja deveria ter se alistado há {} anos. \nSeu alistamento foi em {}'.format((idade - 18), alista))
elif idade < 18:
    print('Seu alistamento sera hein {}'.format(alista))
