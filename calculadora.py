def calculate():
    operation = input('''
Por favor, digite a operação matemática que você gostaria de fazer:
+ se for soma
- se for subtração
* se for multplicação
/ se for divisão
''')

    number_1 = int(input('por favor digite o primeiro numero: '))
    number_2 = int(input('por favor digite o segundo numero: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você não digitou um operador válido, por favor, execute o programa novamente.')

    # Add again() function to calculate() function
    again()

def again():
    calc_again = input('''
quer calcular novamente?
por favor digite S se SIM ou N se NAO.
''')

    if calc_again.upper() == 'S':
        calculate()
    elif calc_again.upper() == 'N':
        print('conta finalizada.')
    else:
        again()

calculate()