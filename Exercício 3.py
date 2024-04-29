'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.'''

letra = str(input('Digite "M" ou "F": '))

if letra in 'Mm':
    print('M - Masculino')
else:
    print('F - Feminino')
