# Aula 019 - Tratamento de Erros e Exceções

"""
Tratamento de erros serve para lidar com situações inesperadas
durante a execução do programa, evitando que ele pare abruptamente.
"""

# Qual a diferença entre erro e exceção? 
"""
Erro é um problema no código, por exemplo, erro de sintaxe (primt(x)). Já a exceção
é um problema durante a excecução, ou seja, em Python, tudo é exceção. Um erro acontece
quando o Python não consegue nem rodar o programa, enquanto a exceção ocorre durante
a execução, isto é, quando o código é valido, mas algo inesperado acontece. 
"""

# Quer encontrar todas as exceções que existem no Python? --> Pesquise por "Python Exception List"

# =====================================================
# O QUE É UM ERRO / EXCEÇÃO
# =====================================================
"""
Uma EXCEÇÃO é um evento que ocorre quando algo dá errado
durante a execução do código.

Exemplos comuns:
- Divisão por zero
- Conversão inválida de tipo
- Acesso a índice inexistente
"""

# Exemplo de erro:
# x = 10 / 0        -> ZeroDivisionError
# int("abc")        -> ValueError
# lista[10]         -> IndexError


# =====================================================
# ESTRUTURA try / except
# =====================================================
"""
A estrutura básica para tratamento de exceções é:
"""

try: # Tente fazer
    x = int("abc")
except ValueError: # Se falhar
    print("Erro: conversão inválida")


# =====================================================
# COMO FUNCIONA
# =====================================================
"""
1. O código dentro do try é executado
2. Se ocorrer um erro:
   - o Python interrompe o try
   - pula para o except correspondente
3. Se não ocorrer erro:
   - o except é ignorado
"""

# Exemplo:
try:
    x = 10 / 2
    print(x)
except ZeroDivisionError:
    print("Divisão por zero")


# =====================================================
# TRATANDO MÚLTIPLAS EXCEÇÕES
# =====================================================
try:
    n = int("abc")
except ValueError:
    print("Erro de valor")
except TypeError:
    print("Erro de tipo")


# Também pode agrupar exceções:
try:
    n = int(None)
except (ValueError, TypeError):
    print("Erro de conversão")


# =====================================================
# BLOCO else
# =====================================================
"""
O bloco else executa SOMENTE se nenhum erro ocorrer no try.
"""

try:
    n = int("10")
except ValueError:
    print("Erro")
else:
    print("Conversão bem-sucedida:", n)


# =====================================================
# BLOCO finally
# =====================================================
"""
O bloco finally SEMPRE é executado,
ocorrendo erro ou não.
"""

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro")
finally:
    print("Fim do tratamento")


# =====================================================
# EXCEÇÃO GENÉRICA (EVITAR)
# =====================================================
"""
Usar 'except:' captura QUALQUER erro,
o que pode esconder problemas reais.
"""

try:
    x = int("abc")
except Exception:
    print("Erro genérico")

# Também podemos atribuir uma variável para o erro

try:
    x = int("abc")
except Exception as erro:
    print(f"Problema encontrado foi: {erro.__cause__}")
    
# Também temos (erro.__cause__, erro.__class__...)

# =====================================================
# CRIANDO EXCEÇÕES COM raise
# =====================================================
"""
É possível lançar exceções manualmente.
"""

def divide(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b


# =====================================================
# EXEMPLO PRÁTICO DE VALIDAÇÃO
# =====================================================
def leiaInt():
    while True:
        try:
            n = int(input("Digite um inteiro: "))
            return n
        except ValueError:
            print("Erro! Digite um número inteiro válido.")


# =====================================================
# RESUMO
# =====================================================
"""
- try: código que pode falhar
- except: trata o erro
- else: executa se não houver erro
- finally: executa sempre
- raise: lança exceções manualmente
- Tratamento evita que o programa quebre
"""
