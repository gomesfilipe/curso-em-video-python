import math
oposto = float(input('Cateto oposto: '))
adjacente = float(input('Cateto adjacente: '))
hipotenusa = math.sqrt(oposto ** 2 + adjacente ** 2)
# hipotenusa = math.hypot(oposto, adjacente)
print('A hipotenusa mede {:.2f}' .format(hipotenusa))
