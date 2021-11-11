print('Gerador de PA')
print('-=' * 12)
termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
c = 0
while c < 10:
    print(termo, '>', end=' ')
    c = c + 1
    termo = termo + razao
print('FIM', end=' ')

