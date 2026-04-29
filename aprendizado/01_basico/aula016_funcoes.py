# Aula 016 - Funções

# Uma função é um bloco de código reutilizável (rotinas) que executa uma tarefa específica. Ela evita repetição de código e melhora organização e legibilidade.

# DEFINIÇÃO:
def nome_funcao(parametros):
    # corpo da função
    valor = 0
    return valor

# def → define a função
# parametros → dados de entrada (opcionais)
# return → valor devolvido (opcional)

# Exemplo:
def soma(a, b):
    return a + b

# OU

def soma(a: int, b: int):
    return a + b

# A diferença é apenas indicativa, pois o python não forçará o tipo nem vai gerar erro. Isso são anotação do tipo type hints, as quais existem para o programador e para as ferramentas, não para o python em tempo de execução. 

# CHAMADA:
argumentos = 0
resultado = nome_funcao(argumentos)

# Exemplo: 
print(soma(3, 7))

# OBS: 
# Parâmetro: variável definida na função
# Argumento: valor passado na chamada

# EMPACOTAMENTO DE PARÂMENTROS:
# Imagine que cada hora você passa uma quantidade de parâmetros diferente para a função, como --> contador(5, 7, 3, 1, 4) e outra hora contador(8, 4, 7). 
# Se, o empacotamento de parâmetros, isso daria erro.
def contador(*num): # O '*' representa o desempacotamento de vários valores (não é ponteiro kkkk). Aqui, Num é uma TUPLA.
    return num * 3

# Perguntinha: Se num é uma tupla, podemos modificar? 
# R: Normalmente não, mas é possível modificar os valores mutáveis da tupla, como listas. Isso, pois você não está modificando a tupla, você está modificando os objetos dentro dela.

# Também temos o desempacotamento de argumentos nomeados: 
def mostra(**kwargs): # Nesse caso, o '**' representa argumentos nomeados, de modo que kwargs é um DICIONÁRIO. 
    print(kwargs)

mostra(nome = 'Ana', idade = 22)

# ATENÇÃO: 
# Se a função não tem return, ela retorna None
# Se retorna um valor, retorna esse valor
# Se retorna vários valores separados por vírgula, retorna uma tupla
# Mas podemos mudar o tipo de retorno colocando (), [] ou assim {}

# MUITO CUIDADO: Toda as passagens de parâmetros em python é atribuição de objeto e não por valor nem por referência (mas é como se fosse por referência), então se muda na função, também muda os mutáveis.
# Desse modo, quando você chama uma função, o que acontece é:
# O nome do parâmetro passa a referenciar o mesmo objeto que o argumento referencia. 

### CONSEQUÊNCIAS ###
# ---> Consequência prática (imutáveis)

# Objetos imutáveis (int, float, str, tuple):

def f(x):
    x = x + 1

a = 10
f(a)
print(a)  # 10

# x passa a referenciar outro objeto
# a continua referenciando o objeto original
# Parece “passagem por valor”, mas não é

# ---> Consequência prática (mutáveis)

# Objetos mutáveis (list, dict, set):

def f(lista):
    lista.append(4)

l = [1, 2, 3]
f(l)
print(l)  # [1, 2, 3, 4]

# A função modifica o mesmo objeto
# O efeito aparece fora da função
# Parece “passagem por referência”, mas não é

# --> Exemplo que confunde muita gente:
def f(lista):
    lista = [0, 0, 0]

l = [1, 2, 3]
f(l)
print(l)  # [1, 2, 3]


# Aqui, lista passa a apontar para outro objeto
# l continua apontando para o original