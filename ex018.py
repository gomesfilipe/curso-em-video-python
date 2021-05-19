import math
angulo = float(input('Digite o angulo '))
angulo = math.radians(angulo)
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print('Seno {:.2f}\nCosseno {:.2f}\nTangente {:.2f}\n' .format(sen, cos, tan))
