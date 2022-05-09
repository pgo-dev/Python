import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))

n = random.sample([a1, a2, a3, a4], k=4)
print(n)

print('\nO primeiro aluno a apresentar é {}'.format(n[0]))
print('O segundo aluno a apresentar é {}'.format(n[1]))
print('O terceiro aluno a apresentar é {}'.format(n[2]))
print('O quarto aluno a apresentar é {}'.format(n[3]))
