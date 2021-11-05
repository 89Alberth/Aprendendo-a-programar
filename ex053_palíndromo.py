frase = str(input('Digite uma frase: ')).strip().upper() #desconsidera os espaço antes a após a frase e coloca tudo maiúsculo
palavras = frase.split()     #divide as frase
junto = ''.join(palavras)    # junta as frase eliminando os espaços
inverso = ''                 # serve como um contador para o FOR
for letra in range(len(junto) - 1, -1, -1):   
    inverso = inverso + junto[letra]
if junto == inverso:
    print('Está frase e  um palíndromo')
else:
     print('Não é um palídromo')
print(junto)
print(inverso)