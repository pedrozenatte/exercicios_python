# Aula 005 - Manupulando cadeias de texto

# Uma cadeia de texto é uma string e, no python, fica entre aspas simples '' ou aspas duplas "". 

# frase = 'Python', mas o que ocorre é o que acontece em linguagem C,isto é, é separado em um vetor de caracteres, de modo que cada letra fica alocada em uma posição contígua da memória

# --- FATIAMENTO ---

# frase[3] --> mostra apenas o caractere da posição de índice 3 do vetor. 
# frase[2:5] --> pega da posição de índice 2 até a posição de índice 5-1 (uma a abaixo da posição final indicada).
# frase[2:10:2] -->  aqui ele vai de 2 até 10-1 pulando de 2 em dois.
# frase[:5] --> quando omitimos o início, ele vai do índice 0 até o índice 4.
# frase[15:] --> quando mitimos o final, ele vai do índice 15 até o final.
# frase[15::3] --> nesse caso, ele vai do índice 15 até o final, pulando de 3 em 3.

# --- ANÁLISE ---

# len(frase) --> conta a quantidade de caracteres que tem no "vetor".
# frase.count('o') --> conta quantas vezes aparece a letra "o" na frase.
# frase.count('o', 0, 13) --> conta quantos "o" aparecem, mas já está considerando um fatiamento que começa em 0 e vai até o 13-1.
# frase.find('deo') --> conta quantas vezes foi encontrado o "deo" na frase, e mostra a posição que começa a subfrase. Caso não tenha a substring na string, é retornado o valor -1.
# 'Python' in frase --> Indica se é verdadeiro ou falso, isto é, se a string 'Python' está ou não na frase. 

# --- TRANSFORMAÇÃO ---

# frase.replace('Python', 'Android') --> vai procurar por Python na frase e substituir por Android.
# frase.upper() --> pega o que está em minúsculo e deixa em maiúsculo.
# frase.lower() --> faz o contrário do upper. 
# frase.capitalize() --> pega tudo, deixa em minúsculo, e depois coloca apenas a primeira letra da string total como maiúsculo.
# frase.title() --> pega tudo, deixa em minúsculo, e depois aplica o capitalize() para cada palavra, ou seja, cada palavra da string terá a primeira letra como maiúsculo.
# frase.replace(antigo, novo) --> procura todas as ocorrências de "antigo" e troca por "novo" retornando uma nova string, sem modificar a original. 

# Vamos supor: frase =    Aprendendo Python     
# frase.strip() --> Remove todos os espaços inúteis, isto é, os espaçamentos no início e no final que estão atoa.
# frase.rstrip() --> o r é de right, então começa pela direita e remove apenas os espaços inúteis da direita.
# frase.lstrip() --> o l é de left, então começa pela esquerda e remove apenas os espaços inúteis da esquerda.

# --- DIVISÃO ---

# frase.split() --> quebra a string onde houver espaços (ou outro separador, se informado) e devolve uma lista contendo cada pedaço isolado. É usado para transformar uma frase em palavras individuais ou separar elementos de um texto de forma estruturada.

# --- JUNÇÃO ---

# '-'.join(frase) --> '-'.join(frase) une os elementos de uma sequência (como uma lista de palavras) colocando um hífen entre cada elemento. OBS: o que está entre aspas simples é o separador que será usado.

frase = 'Curso em Vídeo Python'
print(frase[1:15:2])

# Quando queremos printar um texto muito grande em várias linhas, podemos colocar em 3 aspas duplas:

print("""Nesse caso
      ele considera as quebras
      de linha, e não coloca tudo em 
      uma única linha\n\n\n""")

# OBS: No python tudo é um objeto, então funciona talcoisa.método()

print(frase.upper().count('O'))

# Uma string é imutável, então não tem como:
# frase[0] = J
# pois ela é imutável, a única maneira de mexer é com o .replace:

print(frase.replace('Python', 'Android'))
# MAS ATENÇÃO, ela o replace não modifica a frase, apenas aquela instância, pois se fizer:
frase.replace('Python', 'Android')
print(frase)
# Perceba que a frase não mudou, teria que salvar em alguma variável a mudança, por exemplo:
frase = frase.replace('Python', 'Android')
print(frase)
# Nesse caso, ocorre a mudança

