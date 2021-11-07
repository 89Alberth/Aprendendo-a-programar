sexo = str(input('Informe seu sexo [M] ou [F]: ')).strip()
while sexo not in 'mfMF':
    sexo = str(input('Opção inválida,por favor informe seu sexo: '))
print('Cadastro realizado com sucesso!')