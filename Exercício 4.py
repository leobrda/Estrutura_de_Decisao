'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

letra = str(input('Digite uma letra qualquer: ')).strip()
if letra in 'aeiou':
    print('É uma VOGAL!')
else:
    print('É uma CONSOANTE!')

