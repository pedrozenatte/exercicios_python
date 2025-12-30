# Referente a aula013

# Crie um programa em que o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista la dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

valores_numericos = []

# Critério de parada será o "-"
while True:    
    valor = input('Valor: ')

    if valor == '-': 
        break
    
    if float(valor) not in valores_numericos:
        valores_numericos.append(float(valor))
        print(f'{valor} adicionado')

    else:
        print(f'Não foi possível adicionar, valor já existente') 

valores_numericos.sort()
print(valores_numericos)


        


    