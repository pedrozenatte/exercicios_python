# Referente a aula012

# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)

tupla = (n1, n2, n3, n4, n5) # Poderia ter colocado a função direto na tupla, como "tupla = (randint(0, 10)...)"
maior = max(tupla)
menor = min(tupla)

print(tupla)
print(f'Menor: {menor}\nMaior: {maior}')