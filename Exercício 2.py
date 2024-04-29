'''Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.'''

n = float(input('Digite qualquer valor: '))

if n > 0:
    print('VALOR POSITIVO!')
elif n == 0:
    print('VALOR NULO!')
else:
    print('VALOR NEGATIVO!')