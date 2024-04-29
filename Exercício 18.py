'''Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.'''

data = input("Digite uma data no formato dd/mm/aaaa: ")

# Verifica se a entrada possui três elementos separados por "/"
if "/" not in data or len(data.split("/")) != 3:
    print("A data inserida não é válida.")
else:
    # Separa dia, mês e ano
    dia, mes, ano = map(int, data.split('/'))
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    # Verifica se o mês está dentro do intervalo válido
    if mes < 1 or mes > 12:
        print("A data inserida não é válida.")
    else:
        # Verifica se o dia está dentro do intervalo válido para cada mês
        if mes in (1, 3, 5, 7, 8, 10, 12):
            if dia < 1 or dia > 31:
                print("A data inserida não é válida.")
            else:
                print("A data inserida é válida.")
        elif mes in (4, 6, 9, 11):
            if dia < 1 or dia > 30:
                print("A data inserida não é válida.")
            else:
                print("A data inserida é válida.")
        else:
            # Verifica se é um ano bissexto e se o dia está dentro do intervalo válido
            if bissexto:
                if dia < 1 or dia > 29:
                    print("A data inserida não é válida.")
                else:
                    print("A data inserida é válida.")
            else:
                if dia < 1 or dia > 28:
                    print("A data inserida não é válida.")
                else:
                    print("A data inserida é válida.")