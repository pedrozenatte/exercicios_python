# Referente a aula012

# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9.
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
n4 = int(input('Quarto valor: '))

tupla = (n1, n2, n3, n4)

print(tupla)
print(f'O valor 9 apareceu: {tupla.count(9)}')

if tupla.count(3) != 0: # "if 3 in tupla" é uma forma mais pythoniana
    print(f'O valor 3 apareceu primeiro na posição: {tupla.index(3) + 1}°')
else: 
    print('Não existe o valor 3 na lista')

print('Os pares são: ')
# Pares
for i in tupla:
    if i % 2 == 0:
        print(f'{i} ', end='')
print()