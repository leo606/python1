n = float(input('quantos reais voce tem? R$ '))
dolares = n / 3.27
print(type(dolares))
print('com R${:.2f} voce pode comprar ${:.2f}' .format(n, dolares))
