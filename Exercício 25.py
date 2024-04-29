'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

resp_sim = 0

print('Responda as perguntas abaixo com "SIM" ou "NÃO".')
if input('Telefonou para a vítima?').upper() == 'SIM':
    resp_sim = resp_sim + 1
if input('Esteve no local do crime?').upper() == 'SIM':
    resp_sim = resp_sim + 1
if input('Mora perto da vítima?').upper() == 'SIM':
    resp_sim = resp_sim + 1
if input('Devia para a vítima?').upper() == 'SIM':
    resp_sim = resp_sim + 1
if input('Já trabalhou com a vítima?').upper() == 'SIM':
    resp_sim = resp_sim + 1

if resp_sim == 2:
    print('SUSPEITO(A)!')
elif 3 <= resp_sim <= 4:
    print('CÚMPLICE!')
elif resp_sim == 5:
    print('ASSASSINO!')
else:
    print('INOCENTE!')




