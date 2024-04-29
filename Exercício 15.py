'''Faça um Programa que peça os 3 lados de um triângulo.
O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''

l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('O triângulo pode ser FORMADO!')
else:
    print('O triângulo NÃO pode ser formado!')

#Verificando o tipo do triângulo
if l1 == l2 == l3:
    print('TRIÂNGULO EQUILÁTERO!')
elif l1 != l2 != l3 != l1:
    print('TRIÂNGULO ESCALENO!')
else:
    print('TRIÂNGULO ISÓSCELES!')
