'''Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.'''

n = int(input('Digite um número de 1 a 7: '))

if n == 1:
    print('1 - Domingo')
elif n == 2:
    print('2 - Segunda-feira')
elif n == 3:
    print('3 - Terça-feira')
elif n == 4:
    print('4 - Quarta-feira')
elif n == 5:
    print('5 - Quinta-feira')
elif n == 6:
    print('6 - Sexta-feira')
elif n == 7:
    print('Sábado')
else:
    print('Valor inválido. Tente novamente.')