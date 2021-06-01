kms = float(input('quantos Kms foram percorridos?'))
dias = int(input('quantos dias de aluguel?'))
print('o preço a pagar é R$ {:.2f}' .format((kms * 0.15) + (dias * 60)))
