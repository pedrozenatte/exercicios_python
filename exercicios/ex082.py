# Referente a aula013

# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

total = []
pares = []
impares = []

while True: 
    valor = input('Valor: ')

    if valor == '-':
        break
    
    total.append(float(valor))

for i in range(len(total)):
    if total[i] % 2 == 0: # Par
        pares.append(total[i])

    else: # Ímpar
        impares.append(total[i])

print(f'Total: {total}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
