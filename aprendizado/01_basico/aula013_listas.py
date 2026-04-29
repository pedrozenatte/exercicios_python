# Aula 013 - Listas

# Lista é uma estrutura de dados ordenada, mutável e que pode armazenar valores de tipos diferentes.

lista = [10, 'Ana', 3.5]

# As listas, diferente das tuplas, estão entre CONCHETES []
# As listas são mutáveis e não possuem tamanho definido (existe alocação de memória por trás)

x = i = 10

lista.append(x)     # adiciona no final
lista.insert(i, x)  # insere na posição i
lista.pop()         # remove o último
lista.pop(i)        # remove por índice
lista.remove(x)     # remove por valor (a primeira ocorrência do valor)
lista.clear()       # limpa a lista

# O que acontece se removermos um valor que não existe?
# Vai dar erro kkk

# Funções importantes: 

len(lista)
max(lista)
min(lista)
sum(lista)

valores = list(range(4, 11)) 
# Essa função list, cria uma lista

# OBS: A função sort na lista, ordena ela

# Para criar uma lista: 
valores = list() # OU
valores = []

# ATENÇÃO: Cuidado com a igualdade de listas
a = [2, 3, 4, 5]
b = a 
b[2] = 8 # Essa alteração vai mudar tanto a lista "a" quanto a lista "b"
# Isso acontece, pois quando fazemos b = a (uma lista igual a outra), em python, é feita uma ligação e não uma cópia.

# Para fazer uma cópia de uma lista para outra: 
a = [2, 3, 4, 5]
b = a[:] # Assim é uma cópia de "a" dentro de "b"
b[2] = 8 # Isso vai alterar apenas a lista "b"
