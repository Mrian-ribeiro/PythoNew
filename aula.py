# DECLARAÇÃO DE VARIAVEIS
nome = 'matheus'
semNome = None
idade = 18
altura = 1.73
tipo = True

#EXIBIR CONTEUDO
print('o nome é' ,nome, 'e a idade é' ,idade)
#MODO ATUAL 
print(f'o nome é {nome} e a idade é {idade}')

print(f'o nome é {nome} \n idade é {idade}')

print(f'o nome é: \n {nome} \n idade é: \n {idade}')
# "f" o conector de conteudo que possibilita textos + variavel

print(type(nome))
print(type(idade))
print(type(altura))
print(type(tipo))

#Leitura de uma variavel
meuNome = input('DIGITE SEU NOME: ')
print(f'Bem-Vindo(a): {meuNome}')

#int()
#float()

minhaIdade = int(input('DIGITE SUA IDADE:'))
print(type(minhaIdade))
minhaAltura = float(input('DIGITE SUA ALTURA:'))
print(type(minhaAltura))

#operadores logicos (and, or, not)
idade = 20

if idade >=18 and idade <=65:
    print('idade entre 18 e 65')
else:
    print('fora da idade valida')
print('fim')

#Laços de repetição:
#FOR (LAÇO CONTADO)

for x in range(0,10):
    print(x)