'''Faça um Programa que leia três números e mostre o maior e o menor deles.'''

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

maior = n1
menor = n1
#Verificando se o n2 é maior ou menor
if n2 > maior:
    maior = n2
elif n2 < menor:
    menor = n2

#Verificando se o n3 é maior ou menor
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3

print('O MAIOR número é {}.'.format(maior))
print('O MENOR número é {}.'.format(menor))
