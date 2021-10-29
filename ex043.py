peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('Você esta abaixo do peso.')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 30 >= imc > 25:
    print('SOBREPESO')
elif 30 < imc <= 40:
    print('OBESIDADE')
elif imc >= 40:
    print('OBESIDADE MÓRBIDA')



print('o seu IMC é de {:.2f}.'.format(imc))