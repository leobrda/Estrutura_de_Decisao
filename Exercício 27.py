'''Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total.
Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.'''

kgmorango = float(input('Quantos Kg de Morango? '))
kgmaça = float(input('Quantos Kg de Maça? '))

if kgmorango <= 5:
    preco_mo = kgmorango * 2.50
else:
    preco_mo = kgmorango * 2.20

if kgmaça <= 5:
    preco_ma = kgmaça * 1.80
else:
    preco_ma = kgmaça * 1.50

if (kgmorango + kgmaça) < 8 and (preco_mo + preco_ma) < 25:
    total_mo_ma = preco_mo + preco_ma
    print('{} Kg de Morango + {}Kg de Maça = R${:.2f}.'.format(kgmorango, kgmaça, total_mo_ma))

else:
    total_mo_ma = preco_mo + preco_ma
    desconto = total_mo_ma - (total_mo_ma * 10 / 100)
    print('{}Kg de Morango + {}Kg de Maça = R${:.2f}, e com o desconto de 10% o total fica R${:.2f}.'
          .format(kgmorango, kgmaça, total_mo_ma, desconto))



