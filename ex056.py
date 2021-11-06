mediaidade = 0
maioridade = 0
nomevelho = ''
totmulher = 0

for p in range(1, 5):

    print('----{}ª pessoa----'.format(p))

    nome = str(input('Digite seu nome: ')) .strip()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo[M/F]: ')) .strip()
    mediaidade += idade

    if p == 1 and sexo in 'Mn':
        maioridade = idade
        nomevelho = nome
    if idade > maioridade and sexo in 'Mm':
        maioridade = idade
        nomevelho = nome
    if idade < 20 and sexo in 'fF':
        totmulher += 1

mediaidade = mediaidade / 4

print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homen mais velho tem {} e se chama {}.'.format(maioridade, nomevelho))
print('O total de mulheres com menos de 20 anos são {}.'.format(totmulher))


