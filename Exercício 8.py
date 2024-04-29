'''Faça um programa que pergunte o preço de três produtos
e informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.'''

p1 = float(input('Valor do primeiro produto: '))
p2 = float(input('Valor do segundo produto: '))
p3 = float(input('Valor do terceiro produto: '))

mais_caro = p1
mais_barato = p1

if p2 > mais_caro:
    mais_caro = p2
else:
    mais_barato = p2

if p3 > mais_caro:
    mais_caro = p3
else:
    mais_barato = p3

print('O produto mais BARATO é o que custa R${:.2f}.'.format(mais_barato))
