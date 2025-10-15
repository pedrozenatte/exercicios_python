# Tipos Primitivos


# Desafio 03
# Crie um script que leia dois números e mostre a soma entre eles

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('A soma vale:', n1 + n2)

print('A soma vale {}' .format(n1 + n2))

# Temos: int, float, bool, str

# Vamos analisar o tipo de uma variável
n1 = input('Digite um valor: ')
print(type(n1))

n1 = int(input('Digite um número: '))
print(type(n1))

# Utilidade do .format()
print('A soma de {} e {} vale {}' .format(n1, n2, n1 + n2))

# Para testar um tipo, podemos usar o comando is..., por exemplo, isnull(), isna(), isupper()
n = input('Digite algo: ')
print(n.isupper())