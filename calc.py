valor1 = int(input('digite primeiro valor:'))
valor2 = int(input('digite segundo valor: '))
op = int(input(f'Escolha a opreçao matematica: \n 1 - Soma \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n'))

if op == 1:
    soma = valor1+valor2
    print(f'{valor1}+{valor2}={soma}')
elif op  == 2:
    sub = valor1-valor2
    print(f'{valor1}-{valor2}={sub}')
elif op == 4:
    mult = valor1*valor2
    print(f'{valor1}X{valor2}={mult}')
elif op == 3:
    if valor2==0:
        print(f'Errorrr/divisão por 0')
    else:
        div = valor1/valor2
        print(f'{valor1}:{valor2}={div}')
else:
    print(f'Opração Invalida!!')