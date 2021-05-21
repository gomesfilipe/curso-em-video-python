import random
nome1 = str(input('Digite o nome 1 '))
nome2 = str(input('Digite o nome 2 '))
nome3 = str(input('Digite o nome 3 '))
nome4 = str(input('Digite o nome 4 '))

lista = [nome1, nome2, nome3, nome4]
sorteio = random.choice(lista)
print('O nome sorteado foi {}' .format(sorteio))
