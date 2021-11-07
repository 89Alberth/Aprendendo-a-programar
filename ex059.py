from time import sleep
opção = 0
sair = 0
soma = 0

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
while opção != 5:
    print('-=' * 15)
    print('''
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
    ''')
    opção = int(input('>>>>Escolha sua opção: '))
    if opção == 1:
        soma = valor1 + valor2
        print('{} + {} = {}'.format(valor1, valor2, soma))

    elif opção == 2:
        mult = valor1 * valor2
        print('{} x {} = {}'.format(valor1, valor2, mult))

    elif opção == 3:
        if valor1 > valor2:
            print('O número {} é o maior número'.format(valor1))

        else:
            print('O número {} é o maior número'.format(valor2))

    elif opção == 4:
        print('Informe os números novamente: ')
        sleep(2)
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando o programa...')
        print('-=' * 15)
    else:
        print('>>>Opção inválida<<<')
    sleep(3)

sleep(5)
print('Programa finalizado.Obrigado!')








