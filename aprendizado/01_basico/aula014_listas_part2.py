# Aula 014 - Listas, parte 2

# Vamos juntar uma lista na outra

dados = [] 

dados.append('Pedro')
dados.append(23)

pessoas = list()
pessoas.append(dados[:])

# Podemos fazer toda essa estrutura de uma única vez

pessoas = [['Pedro', 23], ['Maria', 19]]

# Podemos abstrair como uma matriz

print(pessoas[0][0])
print(pessoas[1][1])

# CUIDADO: Se fizer pessoas.append(dados), voce estaria fazendo a mesma coisa que pessoas = dados, e isso não seria uma cópia, isto é, o que mudar em uma lista, automaticamente muda na outra, pois sem o fatiamento, estaria criando uma ligação entre as listas e não copiando valores. 

