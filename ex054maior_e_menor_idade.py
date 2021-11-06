from datetime import date
maiorID = 0
menorID = 0

for c in range(1, 8):
   ano = int(input('Em que ano a  {}ª pessoa nasceu: '.format(c)))
   soma = date.today().year - ano
   if soma >= 18:
      maiorID += 1
   else:
      menorID += 1

print('''Ao todo tivemos {} maior de idade
E {} menores de idade'''.format(maiorID, menorID))
