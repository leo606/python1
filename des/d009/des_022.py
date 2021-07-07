# ler nome completo e mostrar:
# todas as letras upper, e lower
# numero de letras sem contar espacos
# quantas letras tem o primeiro nome

nome = str(input('entre com o nome '))
print('nome em maiusculo - {}'.format(nome.upper()))
print('nome em minusculo - {}'.format(nome.lower()))
print('número de letras', len(''.join(nome.split())))
print('numero de letras do primeiro nome', len(nome.split()[0]))

