'''Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário
a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais.
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.'''

saque = int(input('Deseja sacar quantos reais? R$ '))

if saque <= 600:
    print('Ao sacar a quantia de R${:.2f}, você receberá:'.format(saque))
    notas_cem = saque // 100
    saque = saque % 100

    notas_cinq = saque // 50
    saque = saque % 50

    notas_dez = saque // 10
    saque = saque % 10

    notas_cinco = saque // 5
    saque = saque % 5

    notas_um = saque

    if notas_cem > 0:
        if notas_cem == 1:
            print('{} nota de 100 reais'.format(notas_cem), end=", ")
        else:
            print('{} notas de 100 reais'.format(notas_cem), end=", ")
    if notas_cinq > 0:
        if notas_cinq == 1:
            print('{} nota de 50 reais'.format(notas_cinq), end=", ")
        else:
            print('{} notas de 50 reais'.format(notas_cinq), end=", ")
    if notas_dez > 0:
        if notas_dez == 1:
            print('{} nota de 10 reais'.format(notas_dez), end=", ")
        else:
            print('{} notas de 10 reais'.format(notas_dez), end=", ")
    if notas_cinco > 0:
        if notas_cinco == 1:
            print('{} nota de 5 reais'.format(notas_cinco), end=" e  ")
        else:
            print('{} notas de 5 reais'.format(notas_cinco), end=" e ")
    if notas_um > 0:
        if notas_um == 1:
            print('{} nota de 1 real'.format(notas_um), end=".")
        else:
            print('{} notas de 1 real'.format(notas_um), end=".")
else:
    print('Você não pode sacar R${:.2f}.'.format(saque))


