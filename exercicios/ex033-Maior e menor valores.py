primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

maior = primeiro
if primeiro > segundo and primeiro > terceiro:
    maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro

menor = primeiro
if primeiro < segundo and primeiro < terceiro:
    menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < primeiro:
    menor = terceiro


print('O menor valor digitado é: {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))

