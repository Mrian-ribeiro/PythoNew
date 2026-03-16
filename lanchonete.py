print('Bem-Vindo. Lanchonete Meia-Noite \nBoa-noite escolha seu lanche e Bebida: ')

lanche = int(input('1 - Bauru \n2 - Pizza \n3 - X-galinha \n'))
bebida = int(input('1 - guaraná \n2 - água \n3 - vinho \n'))

if lanche == 1 and bebida == 1 or lanche == 3 and bebida == 2 or lanche == 2 and bebida == 1:
    print(f'pedido indiponivel')
else:
    print(f'Seu pedido está sendo preparado')