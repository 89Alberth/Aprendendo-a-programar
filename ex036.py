casa =  float(input('Qual o valor da casa:R$'))
salario = float(input('Qual o salário do comprador:R$'))
anos =  int(input('Em quanto anos o financiamento: '))
prestaçao = casa / (anos * 12)
minimo = salario * (30 / 100)
print('Para comprar uma casa no valor de R${} em  {} anos,a prestaçao ficará de R${:.2f}'.format(casa, anos, prestaçao))
if prestaçao > minimo:
    print('NEGADO')
else:
    print('APROVADO')