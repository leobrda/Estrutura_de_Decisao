'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário
qual operação ele deseja realizar. O resultado da operação deve ser acompanhado
de uma frase que diga se o número é:
a) par ou ímpar;
b) positivo ou negativo;
C) inteiro ou decimal.'''

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))
print('O que deseja fazer?')
print('[1] SOMAR')
print('[2] SUBTRAIR')
print('[3] DIVIDIR')
print('[4] MULTIPLICAR')
opcao = int(input('Qual operador quer testar?'))

# VERIFICANDO SOMA
soma = n1 + n2
par = soma % 2
if opcao == 1:
    print('{} + {} = {}.'.format(n1, n2, soma))
    if par == 0:
        print('É um número PAR!')
    else:
        print('É um número ÍMPAR!')
    if soma > 0:
        print('É um número POSITIVO!')
    else:
        print('É um número NEGATIVO!')
    if soma == int(soma):
        print('É um número INTEIRO!')
    else:
        print('É um número DECIMAL!')

# VERIFICANDO SUBTRAÇÃO
sub = n1 - n2
par = sub % 2
if opcao == 2:
    print('{} - {} = {}.'.format(n1, n2, sub))
    if par == 0:
        print('É um número PAR!')
    else:
        print('É um número ÍMPAR!')
    if sub > 0:
        print('É um número POSITIVO!')
    else:
        print('É um número NEGATIVO!')
    if sub == int(sub):
        print('É um número INTEIRO!')
    else:
        print('É um número DECIMAL!')

# VERIFICANDO DIVISÃO
div = n1 / n2
par = div % 2
if opcao == 3:
    print('{} / {} = {}.'.format(n1, n2, div))
    if par == 0:
        print('É um número PAR!')
    else:
        print('É um número ÍMPAR!')
    if div > 0:
        print('É um número POSITIVO!')
    else:
        print('É um número NEGATIVO!')
    if div == int(div):
        print('É um número INTEIRO!')
    else:
        print('É um número DECIMAL!')

#VERIFICANDO MULTIPLICAÇÃO
mult = n1 * n2
par = mult % 2
if opcao == 4:
    print('{} * {} = {}.'.format(n1, n2, mult))
    if par == 0:
        print('É um número PAR!')
    else:
        print('É um número ÍMPAR!')
    if mult > 0:
        print('É um número POSITIVO!')
    else:
        print('É um número NEGATIVO!')
    if mult == int(mult):
        print('É um número INTEIRO!')
    else:
        print('É um número DECIMAL!')



