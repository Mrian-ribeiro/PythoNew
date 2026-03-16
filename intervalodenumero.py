# valor = int(input('Digite um numero: '))

# if valor >=100 and valor <=200:
#     print(f'O {valor} está entre 100 e 200')
# else:
#     print(f'O valor é: {valor}')
# print('fim')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
sexo = input('S: \n M - Masculino \n F - Feminino \n')
salario = float(input('Quanto você recebe salário fixo: '))

if idade >= 30 and sexo == 'M':
    abono = 100
elif idade < 30 and sexo == 'M':
    abono = 50
elif idade >= 30 and sexo == 'F':
    abono = 200
elif idade < 30 and sexo == 'F':
    abono = 80

print(f'Nome: {nome} seu salário líquido é de {salario+abono}')