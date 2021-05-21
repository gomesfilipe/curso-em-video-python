from random import shuffle
nome1 = str(input('Nome 1 '))
nome2 = str(input('Nome 2 '))
nome3 = str(input('Nome 3 '))
nome4 = str(input('Nome 4 '))

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)
print('A ordem de apresentação será {}' .format(lista))
