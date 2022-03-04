import os

# Bem-vindo
print()
print('### Este é um mini-projeto de uma simples calculadora bastante limitada em python.')
print('### Pretendo refazer com PyQT5/PyQT6')
print()

print('# 1 - Soma')
print('# 2 - Subtração')
print('# 3 - Multiplicação')
print('# 4 - Divisão')
print('# 5 - Exponenciação')


def home():

    while 1:
        print()
        print('### Escolha o tipo de cálculo desejável: ')
        tipo = input('> ')
        print()

        if tipo.isnumeric():
            tipo = int(tipo)
            if tipo > 5:
                print('### SÓ PERMITIDO QUE VOCÊ ESCOLHA DE 1 A 5.')
        else:
            print('### SÓ PERMITIDO QUE VOCÊ ESCOLHA DE 1 A 5.')

        if tipo == 1:
            num1 = input('# Informe um número: ')
            num2 = input('# Informe um número: ')
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                print(f'### Resultado: {num1 + num2}')
            else:
                print('### É NECESSÁRIO QUE SEJA UM NÚMERO')
        elif tipo == 2:
            num1 = input('# Informe um número: ')
            num2 = input('# Informe um número: ')
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                print(f'### Resultado: {num1 - num2}')
            else:
                print('### É NECESSÁRIO QUE SEJA UM NÚMERO')
        elif tipo == 3:
            num1 = input('# Informe um número: ')
            num2 = input('# Informe um número: ')
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                print(f'### Resultado: {num1 * num2}')
            else:
                print('### É NECESSÁRIO QUE SEJA UM NÚMERO')
        elif tipo == 4:
            num1 = input('# Informe um número: ')
            num2 = input('# Informe um número: ')
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                if num2 == 0:
                    print('### NÃO É POSSÍVEL DIVIDIR POR 0')
                else:
                    print(f'### Resultado: {num1 / num2}')
            else:
                print('### É NECESSÁRIO QUE SEJA UM NÚMERO')
        elif tipo == 5:
            num1 = input('# Informe um número: ')
            num2 = input('# Informe um número: ')
            if num1.isnumeric() and num2.isnumeric():
                num1 = int(num1)
                num2 = int(num2)
                print(f'### Resultado: {num1 ** num2}')
            else:
                print('### É NECESSÁRIO QUE SEJA UM NÚMERO')
home()
