'''Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''

turno = str(input('Em que turno você estuda? M - Matutino, V - Verpertino, N - Noturno: '))

if turno in 'Mm':
    print('BOM DIA!')
elif turno in 'Vv':
    print('BOA TARDE!')
elif turno in 'Nn':
    print('BOA NOITE!')
else:
    print('Período inválido. Tente novamente.')


