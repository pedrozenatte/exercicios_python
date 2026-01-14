# Referente a aula015

# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato. 

dados = {}

dados['nome'] = str(input('Nome do jogador: ')).strip()
dados['partidas jogadas'] = int(input('Partidas jogadas: '))

if dados['partidas jogadas'] <= 0:
    del dados['partidas jogadas']

else: 
    qnt_gols_partida = [None] * dados['partidas jogadas']
    for i in range(dados['partidas jogadas']): 
        qnt_gols_partida[i] = int(input(f'Qtd de gols da partida {i}: '))
    
    dados['gols por partida'] = qnt_gols_partida

    dados['total de gols'] = sum(l for l in dados['gols por partida']) # Ou: sum(qnt_gols_partida)

print('-' * 30)
print(dados)
print('-' * 30)

print(f'Nome: {dados["nome"]}')
if len(dados) == 4:
    print(f'Gols por partida: {dados["gols por partida"]}\nTotal de gols: {dados["total de gols"]}')

    print('-' * 30)
    print(f'O jogador {dados["nome"]} jogou {dados["partidas jogadas"]}.')
    for i in range(dados['partidas jogadas']):
        print(f'     --> Na partida {i + 1}, fez {dados["gols por partida"][i]}')
