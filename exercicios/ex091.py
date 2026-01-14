# Referente a aula015

# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado. 

from random import randint
from time import sleep

colocacao = 1

resultado = {}
for i in range(4):
    resultado[f'jogador {i + 1}'] = randint(1, 6)
    print(f'O jogador {i + 1} tirou {resultado[f"jogador {i + 1}"]}')
    sleep(0.5)


resultado = dict(sorted(resultado.items(), key = lambda item: item[1], reverse = True))
# Utilizei o dict(), pois o sorted retorna uma lista

print('Ranking dos jogadores: ')

for chave, valor in resultado.items():
    print(f'{colocacao}° lugar: {chave} tirou {valor}')
    colocacao += 1
    sleep(0.5)
    
