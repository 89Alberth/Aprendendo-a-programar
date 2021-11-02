c = 0
soma = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        c = c + 1
        soma = soma + n
print('A soma entre todos os {} numeros impar de 1 à 500 divivisivel por 3 é {}'.format(c, soma))
