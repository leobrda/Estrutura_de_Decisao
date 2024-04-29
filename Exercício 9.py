'''Faça um Programa que leia três números e mostre-os em ordem decrescente.'''

import math

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

lista = [n1, n2, n3]
decrescente = sorted(lista, reverse=True) # maior pro menor | reverse=False - menor pro maior
print(decrescente)