def metade(n):
    res = n + (n / 2)
    return res


def dobro(n):
    res = n * 2
    return res


def aumentar(n, t):
    res = n + (n * t / 100)
    return res


def diminuir(n, t):
    res = n - (n*t/100)
    return res


def moedas(n):
    res = (f'R${n:.0f},00')
    return res


def leiaint(msg):
    while True:
        n = input(msg)