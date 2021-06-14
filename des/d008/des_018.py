# mostrar o valor do seno, cosseno, tangente do angulo

from math import radians, cos, sin, tan

angulo = float(input('entre com um ângulo: '))
seno = sin(radians(angulo))
print(' --- O SENO é {:.2f}'.format(seno))
cosseno = cos(radians(angulo))
print(' --- O COSSENO é {:.2f}'.format(cosseno))
tan = tan(radians(angulo))
print(' --- A TANGENTE é {:.2f}'.format(tan))
