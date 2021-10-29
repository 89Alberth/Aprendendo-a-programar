dias = float(input('Quantos dias de aluguel: '))
km = float(input('Quantos quilômetro percorrido: '))
total = (dias * 60) + (km * 0.15)
print("-" * 20)
print('O valor a ser pago e de R${}.'.format(total))
pago = float(input('Valor pago: R$'))
troco = pago - total
print('Troco: R$ {:.2f}'.format(troco))
