'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.'''

n = float(input('Digite um número qualquer: '))
if n == int(n):
    print('{} é um número INTEIRO!'.format(n))
else:
    print('{} é um número DECIMAL!'.format(n))

