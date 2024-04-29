'''Faça um Programa que leia um número inteiro menor que 1000 e imprima
a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros.
Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16'''

'''PESQUISAR MAIS SOBRE'''
num = int(input('Digite um número inteiro: '))

if num < 1000:
    centenas = num // 100
    dezenas = (num % 100) // 10
    unidades = (num % 100) % 10

    if centenas > 0:
        if centenas == 1:
            print('{} centena'.format(centenas), end=", ")
        else:
            print('{} centenas'.format(centenas), end=", ")

    if dezenas > 0:
        if dezenas == 1:
            print('{} dezena'.format(dezenas), end=" e ")
        else:
            print('{} dezenas'.format(dezenas), end=" e ")
    if unidades > 0:
        if unidades == 1:
            print('{} unidade.'.format(unidades))
        else:
            print('{} unidades.'.format(unidades))
else:
    print('Número inválido. Tente novamente.')




