# Só pra não dar azar
print('Olá, Mundo!')

# Resultado é a soma
print(7 + 4)

# Resultado é a concatenação
print('7' + '4')

# Podemos usar '+' ou ',', porém depende 
# O '+' é para mostrar uma mensagem e outra mensagem, já a vírgula é uma mensagem e um número
print('Olá', 7)

# Permitir o usuário colocar valores em variáveis
nome = input('Qual é o seu nome?\n')
print(nome)



#####################
# Desafio 01
# Crie um script Python que leia o nome de uma pessoa e mostra uma mensagem de boas-vindas de acordo com o valor digitado.
print('DESAFIO 01\n')

nome = input('Qual é o seu nome?\n')
print('Olá', nome + '! Prazer em te conhecer!')

# Desafio 02
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostra uma mensagem com a data formatada.
print('DESAFIO 02')

dia = input('DIA:')
mes = input('MÊS:')
ano = input('ANO:')
print('Data:', dia + '/' + mes + '/' + ano)

# Desafio 03
# Crie um script que leia dois números e mostre a soma entre eles
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

print('A soma vale:', n1 + n2)
# O input() considera qualquer coisa que entrar como str

# Só na aula 002 e resolvido o problema