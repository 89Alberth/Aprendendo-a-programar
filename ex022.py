#digite o nome
nome = str(input('Digite seu nome: ')).strip()
#Analisando  seu nome...
print('Analisando seu nome...')
#nome em maiusculo
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
#nome em minusculo
print('Seu nome em minúsculo é {}'.format(nome.lower()))
#quantas letra possui o nome sem espaços
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))
#qual e o primeiro nome quantas letras tem
print('Seu primeiro nome  tem {} letras'.format(nome.find(' ')))
