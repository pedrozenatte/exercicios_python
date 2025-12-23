# Referente a aula012

# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de collocação. Depois mostre: 
# Apenas os 5 primeiros colocados.
# Os últimos 4 colocados da tabela.
# Uma lista comos times em ordem alfabética.
# Em que posição na tabela está o time do São Paulo. 

brasileirao = (
    'Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo',
    'Red Bull Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza',
    'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco',
    'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG'
)

print(f'Cinco primeiros colocados: {brasileirao[:5]}')
print(f'Últimos quatro colocados: {brasileirao[16:]}')
print(f'Lista ordenada: {sorted(brasileirao)}')
print(f'São Paulo está na posição: {brasileirao.index("São Paulo") + 1}° posição')
