'''Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
a) até 20 litros, desconto de 3% por litro
b) acima de 20 litros, desconto de 5% por litro
Gasolina:
c) até 20 litros, desconto de 4% por litro
d)acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos,
o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do
litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.'''

litros = float(input('Quantos litros deseja abastecer? '))
tipo = str(input('Álcool ou Gasolina [A/G]? ')).strip()

total_a = litros * 1.90
total_g = litros * 2.50

# TOTAL A PAGAR ÁLCOOL
if tipo in 'Aa':
    if litros <= 20:
        desconto_a = total_a - (total_a * 3 / 100)
    else:
        desconto_a = total_a - (total_a * 5 / 100)
    print('Você abasteceu {} litros de álcool e o total a pagar é R${:.2f}.'.format(litros, desconto_a))

# TOTAL A PAGAR GASOLINA
elif tipo in 'Gg':
    if litros <= 20:
        desconto_g = total_g - (total_g * 4 / 100)
    else:
        desconto_g = total_g - (total_g * 6 / 100)
    print('Você abasteceu {} litros de gasolina e o total a pagar é R${:.2f}.'.format(litros, desconto_g ))

else:
    print('Opção inválida. Tente novamente.')


