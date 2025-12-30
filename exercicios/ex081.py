# Referente a aula013

# Crie um programa que vai ler vários números e colocar em uma lista. Depois mostre: 
# Quantos números foram digitados.
# A lista de valores odernada de forma decrescente.
# Se o valor 5 foi digitado e está ou não na lista. 


numeros = []
contador = 0

while True:
    valor = input('Valor: ')

    if valor == '-':
        break

    numeros.append(float(valor))
    contador += 1


numeros.sort(reverse = True)

print(f'{contador} digitados')

print(numeros)

if 5 in numeros:
    print('O valor 5 foi digitado e está na lista')

else:
    print('O valor 5 não foi digitado, portanto não está na lista')