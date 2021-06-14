import math

catop = float(input('entre com o cateto oposto '))
catad = float(input('entre com o cateto adjacente '))
hip = math.sqrt((catop**2) + (catad**2))
print('o valor da hipotenusa é {}'.format(hip))
