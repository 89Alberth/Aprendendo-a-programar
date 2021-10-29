#perguntar 2 notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

#somar e dividir por 2 as 2 notas
media = (nota1 + nota2) / 2
print('Sua nota é {}.'.format(media))

#se a media for menor que 5 reprovado
if media < 5:
    print('Você esta REPROVADO.')

#se for entre 5 e 6,9 de recuperação
elif 7 > media >= 5:
    print('Você esta de RECUPERAÇÃO')

#se nota for 7 ou mais aprovado
elif media >= 7:
    print('Você está APROVADO.')