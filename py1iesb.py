"""
py1IESB.ipynb
"""

variavel1 = 10
variavel2 = 3
variavel3 = variavel1 + variavel2
print(variavel3)


name = 'Caio'
age = '23'
alive = True

print(name + ' tem ' + age + ' e está vivo?', alive)
print('{} tem {} e está bem q só? {}'.format(name, age, alive))

a = 1
b = a
a = 2

print(a)
print(b)

aNone = None
print(aNone)

idade = int(input('Qual é sua idade? '))
if idade >= 18:
    print('Você pode dirigir')
else:
    print('voce é menor de idade')
