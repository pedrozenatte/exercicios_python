# Aula 008 - Condições aninhadas

# Se - if
# senão se - elif
# senão - else

nome = input('Qual é seu nome? ')

if nome == 'Pedro':
    print('Nome bonito!')

elif nome == 'Gustavo':
    print('Nome popular')

elif nome in ('Ana Cláudia Jéssica Juliana'):
    print('Nome feminino')

else: 
    print('Nome normal')