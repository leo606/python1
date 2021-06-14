from math import hypot

catop = float(input('entre com o cateto oposto '))
catad = float(input('entre com o cateto adjacente '))
hip = hypot(catop, catad)
print('o valor da hipotenusa é {}'.format(hip))
