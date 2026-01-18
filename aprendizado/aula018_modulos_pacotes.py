# Aula 018 - Módulos e Pacotes

# Surgiu no ínicio da década de 60, pois os sistemas estavam ficando cada vez maiores. Nesse sentido, o foco foi dividir um programa grande em pequenos módulos. Isso aumenta a legibilidade e facilita a manutenção. 

# Python organiza código usando módulos e pacotes para facilitar reutilização, organização e manutenção.


# =====================================================
# MÓDULO
# =====================================================
"""
Um MÓDULO é qualquer arquivo com extensão .py.

Ele pode conter:
- variáveis
- funções
- classes
"""

# Exemplo: arquivo matematica.py
def soma(a, b):
    return a + b


# -----------------------------------------------------
# IMPORTANDO UM MÓDULO
# -----------------------------------------------------
"""
Existem várias formas de importar módulos.
"""

import math
print(math.sqrt(16))

from math import sqrt
print(sqrt(16))

import math as m
print(m.sqrt(16))


# =====================================================
# PACOTE -- Também conhecidos como bibliotecas
# =====================================================
"""
Um PACOTE é uma pasta que contém vários módulos Python.

Estrutura típica:

meupacote/
│── __init__.py 
│── modulo1.py
│── modulo2.py
"""

# ATENÇÃO: Todo pacote precisa ter o arquivo __init__.py em primeiro

# Exemplo de importação de pacote
# import meupacote
# from meupacote import modulo1
# from meupacote.modulo2 import funcao


# -----------------------------------------------------
# __init__.py
# -----------------------------------------------------
"""
O arquivo __init__.py indica que a pasta é um pacote.
Ele pode estar vazio ou conter código de inicialização.
"""

# Exemplo de __init__.py
# from .modulo1 import soma

# O arquivo __init__.py fica sempre vazio?
# R: NÃO!

# Exemplo: 

"""
Estrutura de um pacote chamado 'numeros':

numeros/
├── __init__.py
└── fatorial.py
"""

# =====================================================
# MÓDULO fatorial.py
# =====================================================
def fatorial(n):
    """
    Calcula o fatorial de um número inteiro n.
    """
    fat = 1
    for i in range(1, n + 1):
        fat *= i
    return fat


# =====================================================
# __init__.py PODE FICAR VAZIO?
# =====================================================
"""
SIM, o arquivo __init__.py pode ficar vazio.

Nesse caso, o pacote apenas indica sua existência.
O acesso às funções será feito via módulo.
"""

# Uso:
# from numeros import fatorial
# fatorial.fatorial(5)


# =====================================================
# __init__.py EXPONDO FUNÇÕES (RECOMENDADO)
# =====================================================
"""
O __init__.py pode definir a interface pública do pacote.

Exemplo de conteúdo do __init__.py:
"""

# from .fatorial import fatorial

# Uso:
# from numeros import fatorial
# fatorial(5)


# =====================================================
# __init__.py EXPONDO MÓDULOS
# =====================================================
"""
Também é possível expor o módulo inteiro.
"""

# from . import fatorial

# Uso:
# from numeros import fatorial
# fatorial.fatorial(5)


# =====================================================
# BOAS PRÁTICAS
# =====================================================
"""
- __init__.py define a API do pacote
- Não é obrigatório ficar vazio
- Use para facilitar o uso do pacote
- Evite lógica pesada no __init__.py
"""



# =====================================================
# BIBLIOTECA PADRÃO
# =====================================================
"""
Python vem com vários módulos prontos (biblioteca padrão).
"""

import sys
import os
import datetime


# =====================================================
# PACOTES EXTERNOS
# =====================================================
"""
Pacotes externos são instalados com pip.
"""

# pip install requests
# import requests


# =====================================================
# COMO PYTHON ENCONTRA MÓDULOS
# =====================================================
"""
Python procura módulos nesta ordem:
1. Diretório do script atual
2. Diretórios da variável PYTHONPATH
3. Diretórios padrão da instalação do Python
"""

import sys
print(sys.path)


# =====================================================
# MÓDULO vs PACOTE
# =====================================================
"""
Módulo:
- Um arquivo .py
- Unidade básica de código

Pacote:
- Uma pasta com módulos
- Agrupa módulos relacionados
"""

# Quando criamos um módulo, não é recomendado importar usando "from módulo import função", pois caso importemos vários módulos e existir dois módulos com funções diferentes mas com nomes iguais, a última a ser importada é a que prevalece, ou seja, existe o risco de conflito de funções. 

# Vantagens: 
"""
Organização do código
Facilidade na manutenção
Ocultação de código detalhado
Reutilização em outros projetos
"""




##########################################################
# Fazendo uma analogia, um pacote é um .h em C, e os módulos são os .c do .h 

"""
API (Application Programming Interface)

Uma API é uma INTERFACE que define COMO um software pode ser usado
por outros códigos, sem que seja necessário conhecer sua implementação interna.
"""

# =====================================================
# DEFINIÇÃO
# =====================================================
"""
API significa Application Programming Interface.

Ela é um conjunto de:
- funções
- classes
- métodos
- regras de uso

que um sistema disponibiliza para que outro sistema o utilize.
"""

# =====================================================
# IDEIA CENTRAL
# =====================================================
"""
A API é um CONTRATO.

Ela diz:
- o que pode ser usado
- como chamar
- o que esperar como retorno

sem expor como tudo é implementado por dentro.
"""

# =====================================================
# EXEMPLO SIMPLES EM PYTHON
# =====================================================
"""
Considere o pacote 'numeros' com uma função fatorial.
"""

# numeros/fatorial.py
def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)

"""
Aqui, a API é:
- função: fatorial(n)
- parâmetro: n
- retorno: int
"""

# O usuário NÃO precisa saber como o cálculo é feito
# Apenas chama:
# fatorial(5)


# =====================================================
# API EM PACOTES PYTHON
# =====================================================
"""
Em pacotes Python, a API é definida principalmente no __init__.py.

Ele controla o que o usuário pode importar e usar.
"""

# Exemplo de __init__.py
# from .fatorial import fatorial

# API pública:
# numeros.fatorial()


# =====================================================
# API vs IMPLEMENTAÇÃO
# =====================================================
"""
Implementação:
- Código interno
- Pode mudar

API:
- Interface pública
- Deve ser estável
"""

# Mudar implementação NÃO deve quebrar a API
# Mudar a API quebra quem usa o código


# =====================================================
# API DE BIBLIOTECAS PADRÃO
# =====================================================
"""
Exemplos de APIs que você já usa:
"""

import math
math.sqrt(16)

# import list
# list.append(), list.pop() são parte da API da lista


# =====================================================
# RESUMO
# =====================================================
"""
- API = interface de uso do código
- Define o CONTRATO entre códigos
- Esconde implementação interna
- Facilita manutenção e reutilização
- Em Python, __init__.py ajuda a definir a API de pacotes
"""
# API é o “jeito certo” de usar um código, sem saber como ele funciona por dentro.



###############################################################
###############################################################

"""
Em python, não dá para "inibir de verdade" que alguém acesse funções de um módulo que deveriam ser privadas, por exemplo:
Tenho um pacote cadastrar com o módulo cadastro. Nesse módulo, existem 4 funções, duas
funções são as que eu gostaria que o usuário utilizasse (principais), mas duas delas são
apenas funções auxiliares para as duas principais. Para "omitir" as auxiliares, no
__init__.py, é colocado: 
"""

# API para cadastrar

# from ._cadastro import casdastrar
# from ._cadastro import lerArquivo

"""
Porém, quando o usuário importa o pacote, por exemplo: import cadastrar
ele vai poder fazer cadastrar.func1 ou cadastrar.func2, e nesse caso ele não tem acesso 
ao cadastrar.func3 nem cadastrar.func4 (considerando func3 e func4 as funções aux)
PORÉM, a IDE (como o VSCode) fica sugerindo ao usuário de primeira utilizar cadastrar
cadastro para acessar todas as funções possíveis (func1, 2, 3 e 4).
Para evitar isso, pois não tem como evitar o usuário de acessar cadastrar.cadastro, 
coloque o nome do módulo com um underscore (_modulo.py), por exemplo, _cadastro.py
e no __init__.py coloque:
"""

# from .cadastro import func1, func2

__all__ = ["func1", "func2"]  

# por exemplo 

# EXEMPLO: 
#from .cadastro import cadastrar, lerArquivo

__all__ = ["cadastrar", "lerArquivo"]

"""
Além disso, deixe funções internas com _ também isso ajuda as IDEs a sugerirem só 
o que está em __all__.
"""