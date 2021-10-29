n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Prazer em conhecer você!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('E seu ultimo nome é {}'.format(nome[len(nome) - 1]))

