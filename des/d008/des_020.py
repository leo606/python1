import random

alu1 = str(input('primeiro aluno '))
alu2 = str(input('segundo aluno '))
alu3 = str(input('terceiro aluno '))
alu4 = str(input('quarto aluno '))
alu5 = str(input('quinto aluno '))
alu6 = str(input('quinto aluno '))

lista = [alu1, alu3, alu4, alu5, alu6]
random.shuffle(lista)
print(lista)