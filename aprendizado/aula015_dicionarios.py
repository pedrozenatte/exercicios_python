# Aula 015 - Varáveis Compostas (Dicionários)

# Nas listas, tudo necessariamente precisa ser reconhecido por índices, e não por nome, idade ou qualquer outra identificação. Por conta disso, temos os dicionários, que contem índices literais (personalizar os índices)

# Dicionário é uma estrutura de dados que armazena pares chave → valor.

# Dicionários são identificados por: {}

dados = dict() # Dados agora é um dicionário
# OU
dados = {}

# Características principais:
# Não indexado por posição, e sim por chave
# Mutável → pode alterar, adicionar e remover itens
# Chaves são únicas e imutáveis (str, int, tuple)
# Valores podem ser qualquer tipo

# Exemplo:
dados = {'nome': 'Pedro', 'idade': 23} 
# Pedro é o valor e nome é o identificador, e o mesmo ocorre com idade. Agora não temos mais dados[0] e dados[1], temos dados['nome'], dados['idade'].

print(dados['nome']) # Pedro
print(dados['idade']) # 25

# E se quisermos acrescentar mais algum índice, por exemplo, sexo?
# ATENÇÃO: No caso do dicionário, o comando .append() não funciona 
dados['sexo'] = 'M' # Aqui criamos um novo índice

# Para deletar algum elemento: 
del dados['idade']

# RESUMO
# Acesso e modificação
aluno = {'nome': 'Ana', 'idade': 20, 'nota': 8.5} # Declara o dicionário


aluno['nome']        # Acessa valor
aluno['idade'] = 21 # Altera valor
aluno['curso'] = 'Engenharia'  # Adiciona

# Remoção
del aluno['nota']
aluno.pop('idade')

# Percorrer o dicionário
for chave in aluno:
    print(chave, aluno[chave])

for k, v in aluno.items():
    print(k, v) # K é a chave e V é o valor 
# OBS: Para o for, não é possível usar com enumerate(), até por que, o .items() faz esse papel

# Métodos úteis
aluno.keys()    # Chaves
print(aluno.keys) # Printa 
aluno.values()  # Valores
print(aluno.values()) # Printa apenas os valores
aluno.items()   # Pares (chave, valor)
print(aluno.items()) # Printa os dois (chave e valor)

# Quando usar?
# Quando os dados têm significado associado
# Quando acesso por nome é mais claro que por índice
# Representar entidades (pessoa, aluno, produto)

# Dicionário = dados identificados por chave, não por posição.

# ATENÇÃO: Podemos misturar listas, tuplas e dicionários. 

#########################################
# CUIDADO COM O QUE NÃO DEVE SER FEITO:

estado = dict()
brasil = list()

for i in range(3):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado) 

# Isso que foi feito acima equivale ao mesmo problema de duas listas sendo ligadas, apontando para o mesmo endereço de memória. Isto é, o último estado a ser escrito é o que prevalece em todas as 3 iterações. 
# Na lista, resolviamos fazendo:
brasil.append(estado[:]) 
# Porém, nesse caso não funciona, pois é um dicionário, então utilizaremos apenas um:
brasil.append(estado.copy()) # Também é possível fazer isso na lista 


# OBS: Se fizermos x = {'Alface', 'Abacate', 'Laranja'}, isso configura um SET, e um set não é um dicionário. 
# Sets não possuem ordem definida, então ao printar, teremos um resultado não determinístico

# MAS POR QUE QUANDO RODAMOS O SET EM UM IPYNB SEMPRE HÁ A MESMA ORDEM? 
# R: Por que o set é implementado como uma tabela hash, então se estamos em um mesmo processo, uma vez definida as chaves da tabela, sempre serão as mesmas durante todo o processo. Quando executamos um ipynb, o código roda dentro de um kernel, que, nesse contexto, é um processo Python persistente. Enquanto esse kernel permanece ativo, a seed de hash e a estrutura interna do set permanecem as mesmas, fazendo com que o print(set) pareça determinístico, sempre exibindo os elementos na mesma ordem durante aquela sessão. Ao fechar o notebook ou reiniciar o kernel — ou ao executar um script .py, que cria um novo processo Python a cada execução — uma nova seed de hash é utilizada e a tabela interna do set pode ser reorganizada. Por isso, a ordem de impressão pode mudar entre execuções, mesmo que os dados sejam os mesmos.

# Você pode utilizar fstrigs dentro do dicionário, como no exercício 91