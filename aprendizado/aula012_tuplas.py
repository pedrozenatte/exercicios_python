# Aula 012 - Variáveis Compostas (Tuplas)

# Existem em python 3 tipos de variáveis compostas: As tuplas, as listas e os dicionários 

# Toda variável simples é um espaço na memória
# lanche = 'hamburguer'
# lanche = 'suco' 
# O espaço de memória que armazenava o hamburguer passou a armazenar o suco, e o hamburguer foi perdido.

# Como strings são variáveis compostas, então tudo de fatiamento funciona aqui também.

# Uma tupla é uma estrutura de dados ordenada e imutável.
# Ordenada → tem índice (t[0])
# Imutável → não pode alterar, adicionar ou remover elementos
# Pode misturar tipos (int, str, etc.)

# ATENÇÃO: AS tuplas são IMUTÁVEIS

# EXEMPLO: Tuplas fica entre (), MAS podemos fazer sem parênteses que ainda é considerado uma tupla. 

# lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim' # Também é considerado uma tupla
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[3])
print(lanche[-1]) # Nesse caso, o pudim é o lanche[-1], a pizza é o lanche[-2]...

# For mais pythoniano
for comida in lanche: # Forma mais abreviada de fazer "for i in range(len(lanche)):"
    print(f'Eu vou comer {comida}')

# Se quiser mostrar a posição:
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

# enumerate(lanche) é um iterador que percorre a sequência lanche devolvendo dois valores ao mesmo tempo:
# o índice (posição)
# o elemento daquela posição

# Provando imutabilidade (o código a seguir da erro)
# lanche[1] = 'Refrigerante'
# Esse código da erro, pois as tuplas não podem ser alteradas.

print(sorted(lanche)) # sorted() é uma função de ordenação

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b # É a concatenação das duas, sendo os valores de "a" primeiro que os de "b"

print(c)
print(c.index(5)) # Mostra o index do valor 5
# Mas tem dois 5, então falamos para começar na posição 1 (fazemos um deslocamento)
print(c.index(5, 1)) # Dessa forma, será procurado o index do valor 5 começando na posição 1

pessoa = ('Pedro', 39, 'M') # Dados de tipos diferente dentro da mesma tupla
print(pessoa)
del(pessoa) # Deleta a tupla

