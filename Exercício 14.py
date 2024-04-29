'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 0 and media < 4:
    conceito = 'E'
    print('Com as notas {} e {}, sua média foi {}, o conceito {} e você está REPROVADO.'
          .format(nota1, nota2, media, conceito))
elif media >= 4 and media < 6:
    conceito = 'D'
    print('Com as notas {} e {}, sua média foi {}, o conceito {} e você está REPROVADO.'
          .format(nota1, nota2, media, conceito))
elif media >= 6 and media < 7.5:
    conceito = 'C'
    print('Com as notas {} e {}, sua média foi {}, o conceito {} e você está APROVADO.'
          .format(nota1, nota2, media, conceito))
elif media >= 7.5 and media < 9:
    conceito = 'B'
    print('Com as notas {} e {}, sua média foi {}, o conceito {} e você está APROVADO.'
          .format(nota1, nota2, media, conceito))
elif media >= 9 and media <= 10:
    conceito = 'A'
    print('Com as notas {} e {}, sua média foi {}, o conceito {} e você está APROVADO.'
          .format(nota1, nota2, media, conceito))
