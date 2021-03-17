import random
a1 = str(input('entre com um aluno '))
a2 = str(input('entre com um aluno '))
a3 = str(input('entre com um aluno '))
a4 = str(input('entre com um aluno '))

# criar um vetor com os alunos, vetor se cria com []:
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print('o sorteado é {}' .format(sorteado))