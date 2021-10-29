salario = float(input('Qual o sálario do funcionário: R$'))
if salario > 1250:
    aumento = salario + (10 / 100 * salario)
else:
    aumento = salario + (15 / 100 * salario)
print('quem ganhava R${} passára a ganhar R${}.'.format(salario, aumento))
