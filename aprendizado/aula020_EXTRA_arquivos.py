# Aula 20 - Arquivos em Python

"""
Arquivos permitem que um programa leia e grave dados
em armazenamento permanente (disco).
"""

# =====================================================
# O QUE É UM ARQUIVO
# =====================================================
"""
Um arquivo é um conjunto de dados armazenados fora da memória RAM.
Em Python, trabalhamos com arquivos usando a função open().
"""

# =====================================================
# ABRINDO UM ARQUIVO
# =====================================================
"""
Sintaxe:
arquivo = open(nome, modo)
"""

# Exemplos de modos:
# 'r'  -> leitura (read)
# 'w'  -> escrita (write) - sobrescreve o arquivo
# 'a'  -> escrita (append) - adiciona ao final
# 'x'  -> cria arquivo (erro se já existir)
# 'b'  -> modo binário
# 't'  -> modo texto (padrão)
# '+'  -> acrescenta o modo de leitura ou escrita. Exemplo: r+ (leitura e escrita), w+ (escrita e leitura)

# =====================================================
# MODOS COM '+'
# =====================================================
"""
r+  -> leitura + escrita (arquivo DEVE existir)
w+  -> escrita + leitura (APAGA o conteúdo)
a+  -> escrita + leitura (escreve no final)
"""

# =====================================================
# r+  (read + write)
# =====================================================
"""
- Arquivo deve existir
- Não apaga o conteúdo
- Ponteiro começa no início
"""

with open("arquivo.txt", "r+") as f:
    conteudo = f.read()
    f.write("\nNova linha")


# =====================================================
# w+  (write + read)
# =====================================================
"""
- Cria o arquivo se não existir
- APAGA todo o conteúdo existente
- Ponteiro começa no início
"""

with open("arquivo.txt", "w+") as f:
    f.write("Novo conteúdo")
    f.seek(0)
    print(f.read())


# =====================================================
# a+  (append + read)
# =====================================================
"""
- Cria o arquivo se não existir
- NÃO apaga conteúdo
- Escrita SEMPRE no final
- Leitura exige mover o ponteiro
"""

with open("arquivo.txt", "a+") as f:
    f.write("\nLinha adicionada")
    f.seek(0)
    print(f.read())


# =====================================================
# SOBRE O PONTEIRO (seek)
# =====================================================
"""
Ao usar '+', é comum precisar mover o ponteiro.

seek(0) -> início do arquivo
"""

arquivo = open("exemplo.txt", "r")

"""
arquivo.seek(offset, whence)

offset -> deslocamento (quantos bytes mover)
whence -> ponto de referência (opcional)
"""
# Se whence não for informado, o valor padrão é 0

# Mas o que o whence significa exatamente?
"""
whence define DE ONDE o deslocamento será calculado.
"""

# 0 -> início do arquivo (padrão)
# 1 -> posição atual do ponteiro
# 2 -> final do arquivo

# =====================================================
# FUNÇÃO tell()
# =====================================================
"""
tell() retorna a posição atual do ponteiro.
"""

# =====================================================
# FECHANDO UM ARQUIVO
# =====================================================
"""
Todo arquivo aberto deve ser fechado para liberar recursos.
"""

arquivo.close()


# =====================================================
# FORMA CORRETA: with
# =====================================================
"""
A forma recomendada é usar 'with',
pois o Python fecha o arquivo automaticamente.
"""

with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()


# =====================================================
# LEITURA DE ARQUIVOS
# =====================================================

with open("exemplo.txt", "r") as arquivo:
    texto = arquivo.read()        # lê tudo

with open("exemplo.txt", "r") as arquivo:
    linha = arquivo.readline()    # lê uma linha

with open("exemplo.txt", "r") as arquivo:
    linhas = arquivo.readlines()  # cria uma lista de linhas


# =====================================================
# ESCRITA EM ARQUIVOS
# =====================================================

with open("saida.txt", "w") as arquivo:
    arquivo.write("Olá, mundo\n")

with open("saida.txt", "a") as arquivo:
    arquivo.write("Nova linha\n")


# =====================================================
# PERCORRENDO UM ARQUIVO
# =====================================================
"""
Arquivos são iteráveis linha por linha.
"""

with open("exemplo.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())


# =====================================================
# ARQUIVOS DE TEXTO vs BINÁRIOS
# =====================================================
"""
Texto:
- strings
- codificação (UTF-8)

Binário:
- bytes
- imagens, PDFs, etc.
"""

with open("imagem.png", "rb") as arquivo:
    dados = arquivo.read()


# =====================================================
# TRATAMENTO DE ERROS COM ARQUIVOS
# =====================================================

try:
    with open("nao_existe.txt", "r") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("Arquivo não encontrado")


# =====================================================
# RESUMO
# =====================================================
"""
- open() abre arquivos
- use 'with' para segurança
- 'r', 'w', 'a' definem o modo
- read(), readline(), readlines() leem dados
- write() grava dados
- arquivos podem ser texto ou binários
"""
