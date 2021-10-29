km = float(input('Qual a distância da sua viagem: '))

if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45

print('Você esta preste a inicia uma viagem de {}KM.'.format(km))
print(('O preço é de R${}.'.format(preço)))
