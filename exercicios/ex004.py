# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele. 

algo = input('Digite alguma coisa: ')

print('O tipo de {} é {}' .format(algo, type(algo)))
print('Só tem espaços?', algo.isspace())
print('É um número? ', algo.isnumeric)
print('É alfabético? ', algo.isalpha())
print('É alfanúmerico? ', algo.isalnum())
print('Está em maiúsculas? ', algo.isupper())
print('Está em minusculas? ', algo.islower())
print('Está capitalizada? ', algo.istitle()) # Significa que é uma mistura de maiúsculas e minúsculas
