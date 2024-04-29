'''O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara
o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra:
tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.'''

quantidade = float(input('Quantos Kg de carne comprou? '))
tipo_carne = str(input('Qual carne comprou [FILE DUPLO/ ALCATRA/ PICANHA]? ')).strip().upper()
tipo_pag = str(input('Qual a forma de pagamento [CARTAO TABAJARA/ DINHEIRO]? ')).strip().upper()

if tipo_pag in 'CARTAO TABAJARA':
    if tipo_carne in 'FILE DUPLO':
        if quantidade <= 5:
            total_fd = quantidade * 4.90
        else:
            total_fd = quantidade * 5.80
        desconto_fd = total_fd - (total_fd * 5 / 100)
        print('Você comprou {}Kg de File Duplo e o total a pagar é R${:.2f}.'.format(quantidade, desconto_fd))

    elif tipo_carne in 'ALCATRA':
        if quantidade <= 5:
            total_a = quantidade * 5.90
        else:
            total_a = quantidade * 6.80
        desconto_a = total_a - (total_a * 5 / 100)
        print('Você comprou {}Kg de Alcatra e o total a pagar é R${:.2f}.'.format(quantidade, desconto_a))

    elif tipo_carne in 'PICANHA':
        if quantidade <= 5:
            total_p = quantidade * 6.90
        else:
            total_p = quantidade * 7.80
        desconto_p = total_p - (total_p * 5 / 100)
        print('Você comprou {}Kg de Picanha e o total a pagar é R${:.2f}.'.format(quantidade, desconto_p))
    else:
        print('Não vendemos esse tipo de carne. Tente novamente.')

elif tipo_pag in 'DINHEIRO':
    if tipo_carne in 'FILE DUPLO':
        if quantidade <= 5:
            total_fd = quantidade * 4.90
        else:
            total_fd = quantidade * 5.80
        print('Você comprou {}Kg de File Duplo e o total a pagar é R${:.2f}.'.format(quantidade, total_fd))
    elif tipo_carne in 'ALCATRA':
        if quantidade <= 5:
            total_a = quantidade * 5.90
        else:
            total_a = quantidade * 6.80
        print('Você comprou {}Kg de Alcatra e o total a pagar é R${:.2f}.'.format(quantidade, total_a))
    elif tipo_carne in 'PICANHA':
        if quantidade <= 5:
            total_p = quantidade * 6.90
        else:
            total_p = quantidade * 7.80
        print('Você comprou {}Kg de Picanha e o total a pagar é R${:.2f}.'.format(quantidade, total_p))
else:
    print('Não aceitamos esse tipo de pagamento. Escolha outra forma.')



