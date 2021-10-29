from datetime import date
print('''Você é:
[1]Homen
[2]Mulher''')

sexo = int(input('Escolha seu gênero: '))

if sexo == 2:
    print('Você não precisa se alistar')

else:
    atual = date.today().year
    nasc = int(input('Digite o ano de nascimento: '))
    idade = atual - nasc

    if idade == 18:
       print ('Você deve se alistar IMEDIATAMENTE.')
    elif idade < 18:
       saldo = 18 - idade
       ano = saldo + atual
       print('Ainda não esta no ano do seu alistamento,ainda falta {} anos,você deverá se alistar em {}'.format(saldo, ano))
    elif idade > 18:
      saldo = idade - 18
      ano = atual - saldo
      print('Você passou {} anos para seu alistamento seu alistamento deveria ser em {}'.format(saldo, ano))
