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
            num1 = int(input('# Informe um número: '))
            num2 = int(input('# Informe um número: '))
            print(f'### Resultado: {num1 + num2}')
        elif tipo == 2:
            num1 = int(input('# Informe um número: '))
            num2 = int(input('# Informe um número: '))
            print(f'### Resultado: {num1 - num2}')
        elif tipo == 3:
            num1 = int(input('# Informe um número: '))
            num2 = int(input('# Informe um número: '))
            print(f'### Resultado: {num1 * num2}')
        elif tipo == 4:
            num1 = int(input('# Informe um número: '))
            num2 = int(input('# Informe um número: '))
            if num2 == 0:
                print('### NÃO É POSSÍVEL DIVIDIR POR 0')
            else:
                print(f'### Resultado: {num1 / num2}')
        elif tipo == 5:
            num1 = int(input('# Informe um número: '))
            num2 = int(input('# Informe um número: '))
            print(f'### Resultado: {num1 ** num2}')
home()