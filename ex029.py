velocidade = float(input('Qual velocidade do carro: '))
multa = (velocidade - 80) * 7

if velocidade > 80:
    print('MULTADO! você excedeu o limite de velocidade.Sua multa é de R${}.'.format(multa))

print('Tenha um bom dia dirija com segurança.')
