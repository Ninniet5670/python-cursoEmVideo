import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo nome: '))
n3 = str(input('Terceiro nome: '))
n4 = str(input('Quarto nome: '))
list = [n1, n2, n3, n4]
rname = random.choice(list)
print(f'E o nome escolhido foi {rname}') 