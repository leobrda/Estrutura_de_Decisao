'''As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo
o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%;
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%;
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%;
- salários de R$ 1500,00 em diante : aumento de 5%.
Após o aumento ser realizado, informe na tela:
a) O salário antes do reajuste;
b) O percentual de aumento aplicado;
c) O valor do aumento;
d) O novo salário, após o aumento.'''

salario = float(input('Digite o seu salário: R$ '))

if salario <= 280:
    percentual = 20
    novo = salario + (salario * 20 / 100)
elif salario > 280 and salario < 700:
    percentual = 15
    novo = salario + (salario * 15 / 100)
elif salario > 700 and salario < 1500:
    percentual = 10
    novo = salario + (salario * 10 / 100)
elif salario >= 1500:
    percentual = 5
    novo = salario + (salario * 5 / 100)

aumento = novo - salario

print('O salário antes do reajuste é R${:.2f}.'.format(salario))
print('O percentual de aumento aplicado foi {}%.'.format(percentual))
print('O valor do aumento foi de R${:.2f}.'.format(aumento))
print('O novo salário, após o aumento é R${:.2f}.'.format(novo))

