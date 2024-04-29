'''Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;'''

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7:
    print('A sua média foi {:.2f} e você está APROVADO!'.format(media))
else:
    print('A sua média foi {:.2f} e você está REPROVADO!'.format(media))
