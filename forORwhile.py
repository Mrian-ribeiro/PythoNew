#Laços de repetição:
#FOR (LAÇO CONTADO)

# for x in range(10):
#     print(x)


# for s in range(5,10):
#     print(s)

# for y in 'rian':
#     print(y)

# for g in enumerate('matheus'):
#     print(g)

#WHILE (LAÇO CONDICIONADO)

valor = 11
while valor<10:
    print(valor)
    valor+=1

while True:
    print('Bem vindo(a)')
    resp = input('Deseja sair S ou N:')
    if resp == 'S':
        break