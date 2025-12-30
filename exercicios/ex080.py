# Referente a aula013

# Crie um programa que o usuário possa digitar cinco valores numericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela. 

valores = []
aux = 0

opcao = int(input('Opção (1 ou 2): '))

if opcao == 1:
    for j in range(5):
        valor = float(input('Valor: '))

        if not valores: # Verifica lista vazia
            valores.append(valor)
        
        else: 
            valores.append(0) # Crescer a lista em uma únidade
            for i in range(len(valores) -2, -1, -1): # -2 para considerar o tamanho antigo
                if valor > valores[i]:
                    valores[i + 1] = valor
                    break

                else: 
                    valores[i + 1] = valores[i]
                    if i == 0: # Valor menor que todos da lista
                        valores[i] = valor

# ------------- OUTRA FORMA DE FAZER EM PYTHON -------------
# A inserção da lista é a criação de um nó a mais que ocupa a posição de inserção, shiftando para a direita o item daquela posição
else:
    for j in range(5):
        valor = float(input('Valor: '))

        if not valores:
            valores.append(valor)

        else: 
            flag = 0 # Se inserir, vira 1
            for i in range(len(valores) -1, -1, -1):
                if valor >= valores[i]:
                    valores.insert(i + 1, valor)
                    flag = 1
                    break
            
            if flag == 0: # Não inseriu, então menor que todos
                valores.insert(0, valor)
        
            
print(valores)

                