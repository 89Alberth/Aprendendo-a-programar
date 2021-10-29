preço = float(input('Qual o valor do produto: R$'))

print('Forma de pagamento:')
print('''
[1] À vista/cheque
[2] À vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
pag = int(input('Escolha a forma de pagamento: '))

if pag == 1:
    total = preço - (preço * 10/100)

elif pag == 2:
    total = preço - (preço * 5/100)

elif pag == 3:
    total = preço

elif pag == 4:
    parcelas = int(input('Quantas parcela deseja: '))
    total = preço + (preço * 20/100)
    valor = total / parcelas
    print('A compra ficara R${} com juros,{} parcelas de R${}.'.format(total, parcelas, valor))
else:
    total = preço
    print('\33[1;31mOpção de pagamento INVÁLIDO.')


print('O produta custa R${}.'.format(total))