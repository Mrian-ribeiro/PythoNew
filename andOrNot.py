#operadores logicos (and, or, not)
idade = int(input('Digite sua idade: '))

if idade >=18 and idade <=65:
    print('idade entre 18 e 65')
else:
    print('fora da idade valida')
print('fim')

if not idade >=18:
    print('menor de idade')
else:
    print('maior de idade')
print('fim')

