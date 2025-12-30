# Referente a aula013

# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

lista = []

for i in range(5):
    lista.append(int(input(f"Valor[{i}]: ")))

maior = max(lista)
menor = min(lista)

print(lista)
print(f"Menor: {menor}\nMaior: {maior}")

posicao_menor = lista.index(menor)
posicao_maior = lista.index(maior)

print(f'Posição menor: {posicao_menor + 1}', end = '')
if lista.count(menor) > 1:
    for i in range(lista.count(menor) - 1):
        posicao_menor = lista.index(menor, posicao_menor + 1)
        print(f'...{posicao_menor + 1}', end = '')
print()

print(f'Posição maior: {posicao_maior + 1}', end = '')
if lista.count(maior) > 1:
    for i in range(lista.count(maior) - 1):
        posicao_maior = lista.index(maior, posicao_maior + 1)
        print(f'...{posicao_maior + 1}', end = '')
print()