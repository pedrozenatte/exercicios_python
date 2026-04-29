# Aula 017 - Funções parte 2: Interactive Help, Docstrings, Argumentos Opcionais, Escopo de Variáveis, Retorno de Resultados.  

# INTERACTIVE HELP
help() 
# --> Escrever isso no terminal do python. Isso abre um outro terminal que ao digitar qualquer função, como print, teremos a explicação completa do funcionamento daquela função ou biblioteca. 
# Basicamente é um manual completo de tudo que vem no python.
# Outra forma é escrever dentro de help(), por exemplo:
help(print)
print(print.__doc__)

# Para sair: 
quit



# DOCSTRINGS
# As docstrings é para justamente escrever como a função que foi criada pelo usuário funciona, isto é, para ser utilizada pelo comando help(função do usuário).
# Docstrings servem para documentar funções, classes, módulos e métodos diretamente no código, de forma padronizada e acessível em tempo de execução.
def contador(i, f, p):
    # As docstrings ficam entre """docstring""" ou '''docstrings'''
    '''
    Faz uma contagem e mostra na tela
    
    :param i: Início da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return: Sem retorno
    '''
    c = i
    while c <= f:
        print(f'{c}', end = '..')
        c += p
    
    print('FIM!')

help(contador) # Isso vai mostrar a docstrings



# PARÂMETROS OPCIONAIS
# Parâmetros opcionais são parâmetros que possuem um valor padrão. Isto é, se o argumento não for passado na chamada da função, o valor padrão é usado.
def soma(a, b = 0):
    return a + b

# a --> Obrigatório
# b --> opcional (valor padrão é 0)
# CUIDADO: Não se deve colocar parâmetros opcionais antes dos parâmetros sem valor padrão.4
# Erro:
# def soma(a = 0, b):  
#     return a + b

# Mas podemos colocar todos os parâmetros opcionais



# ESCOPO DE VARIÁVEIS
# Escopo define onde uma variável pode ser acessada no código.
# Python segue a regra LEGB: Local, Enclosing, Global e Built-in.

"""
- Local: dentro da função
- Enclosing: função externa
- Global: fora de funções
- Built-in: funções padrão do Python
"""
# =========================
# ESCOPO LOCAL
# =========================
def exemplo_local():
    x = 10  # variável local
    print(x)

# print(x)  # ERRO: x não existe fora da função

# =========================
# ESCOPO GLOBAL
# =========================
y = 5  # variável global

def exemplo_global():
    print(y)  # acessa variável global

exemplo_global()
# =========================
# MODIFICANDO VARIÁVEL GLOBAL
# =========================
contador = 0

def incrementa():
    global contador
    contador += 1

# OBS: Se não colocar o global contador, isto é, apenas colocar contador, teremos dois contadores, um local da função e um global fora da função. 

# =========================
# ESCOPO ENCLOSING (função dentro de função)
# =========================
"""
Uma variável ENCLONSING pertence a uma FUNÇÃO EXTERNA quando existe uma função definida dentro de outra função.

Ela NÃO é local da função interna
Ela NÃO é global do programa
Ela fica "fechada" entre as duas funções
"""
def externa():
    x = 10  # variável da função externa

    def interna():
        print(x)  # acessa variável enclosing

    interna()

externa()

# =========================
# MODIFICANDO VARIÁVEL ENCLOSING
# =========================
def externa_mod():
    x = 10

    def interna():
        nonlocal x
        x += 5

    interna()
    print(x)

externa_mod()

# =========================
# ESCOPO BUILT-IN
# =========================
print(len([1, 2, 3]))  # len é built-in

"""
Variáveis BUILT-IN são nomes definidos pelo próprio Python.
Elas estão sempre disponíveis, mesmo sem importação.
"""



# RETORNO DE VALORES
# O retorno de uma função é o valor que ela devolve para quem a chamou, usando a palavra-chave return.
# =========================
# RETORNO BÁSICO
# =========================
def soma(a, b):
    return a + b

resultado = soma(2, 3)
print(resultado)


# =========================
# FUNÇÃO SEM RETURN
# =========================
def f():
    pass 
# OBS: Esse pass é uma instrução nula. Ela não faz nada e existe apenas para satisfazer a sintaxe da linguagem. 

print(f())  # None

# OBS: Existe o escopo de importação também, isto é, importar uma biblioteca dentro de uma função, as funções da biblioteca funcionarão apenas no escopo da função do usuário. 