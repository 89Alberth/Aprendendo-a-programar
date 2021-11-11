print('Super gerado de PA')
print('-=' * 15)
primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
c = 1
opçao = ''
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(termo, '→', end=' ')
        termo += razao
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos a mais você deseja? '))
    
print('FIM')
print('Ao total foram lidos {} termos.'.format(total))

