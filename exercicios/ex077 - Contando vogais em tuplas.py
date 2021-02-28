palavras = ('aprender', 'pregramar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro', 'tecnologia')

for most in palavras:
    print(f'Na palavra {most.upper()} temos  ', end='')

    for letra in most:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()