dicionario = {}

def notas(*n, sit=False):
    """
    -> FUNÇÃO PARA ANALISAR NOTAS E SITUAÇÃO DE VARIOS ALUNOS
    :param n: UMA OU MAIS NOTA DOS ALUNOS (ACEITA VARIAS)
    :param sit: VALOR OPCIONAL, INDICANDO SE DEVE OU NÃO ADICIONAR A SITUAÇÃO
    :return: DICIONARIO COM VARIAS INFORMAÇÕES SOBRE A SITUAÇÃO DE TURMA
    """

    dicionario['total'] = len(n)
    dicionario['maior'] = max(n)
    dicionario['menor'] = min(n)
    dicionario['media'] = sum(n) / len(n)

    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação:'] = 'BOA'
        elif dicionario['media'] >= 5:
            dicionario['situação:'] = 'RAZOAVEL'
        else:
            dicionario['situação:'] = 'RUIM'

    return dicionario

#programa principal
resp = notas(1, 9.5, 9, 6.5, sit=True)
print(resp)
help(notas)

