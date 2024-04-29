'''Faça um programa para o cálculo de uma folha de pagamento,
sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo)
e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
O Salário Líquido corresponde ao Salário Bruto menos os descontos.
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20%
Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00'''

valor = float(input('Quanto você recebe por hora trabalhada? R$ '))
horas = int(input('Quantas horas trabalhadas no mês? '))
salario_bruto = valor * horas
#Desconto do IR
if salario_bruto <= 900:
    print('ISENTO do Imposto de Renda!')
elif salario_bruto <= 1500:
    ir = salario_bruto * 5 / 100
elif salario_bruto <= 2500:
    ir = salario_bruto * 10 / 100
elif salario_bruto > 2500:
    ir = salario_bruto * 20 / 100
#Cálculo do INSS
if salario_bruto <= 900:
    print('ISENTO do INSS!')
elif salario_bruto <= 1500:
    inss = salario_bruto * 10 / 100
elif salario_bruto <= 2500:
    inss = salario_bruto * 10 / 100
elif salario_bruto > 2500:
    inss = salario_bruto * 10 / 100
# Cálculo do FGTS
fgts = salario_bruto * 11 / 100
total_descontos = ir + inss
salario_liquido = salario_bruto - ir - inss

print('Salário Bruto: ({} * {})  :R${:.2f}'.format(valor, horas, salario_bruto))
print('(-) IR (5%)                 :R${:.2f}'.format(ir))
print('(-) INSS (10%)              :R${:.2f}'.format(inss))
print('FGTS (11%)                  :R${:.2f}'.format(fgts))
print('Total de descontos          :R${:.2f}'.format(total_descontos))
print('Salário Líquido             :R${:.2f}'.format(salario_liquido))

