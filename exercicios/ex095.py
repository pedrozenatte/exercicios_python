# Referente a aula015

# Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador. 

dados = {}
jogadores = []


print('-' * 30)
# Condição de parada: '-'
while True: 
    dados['nome'] = str(input('Nome do jogador: ')).strip()

    if dados['nome'] == '-':
        break

    dados['partidas jogadas'] = int(input('Partidas jogadas: '))

    if dados['partidas jogadas'] <= 0:
        del dados['partidas jogadas']

    else: 
        qnt_gols_partida = [None] * dados['partidas jogadas']
        for i in range(dados['partidas jogadas']): 
            qnt_gols_partida[i] = int(input(f'Qtd de gols da partida {i + 1}: '))
        
        dados['gols por partida'] = qnt_gols_partida

        dados['total de gols'] = sum(l for l in dados['gols por partida']) # Ou: sum(l for l in qnt_gols_partida)

    jogadores.append(dados.copy())
    print('-' * 30)

print('=' * 60)
print('DADOS' .center(60))
print('=' * 60)

print(f'{"COD":<5}{"Nome":<15}{"Gols":<15}{"Total":<10}')

for id, j in enumerate(jogadores):
    print(f'{id + 1:<5}{j["nome"]:<15}', end = '')
    if len(j) == 4:
        gols = ' '.join(map(str, j['gols por partida'])) # Essa função está transformando todos os itens de valores da lista j['gols por partida'] em uma str
        print(f'{gols:<15}{j["total de gols"]:<10}')

    else: 
        print(f'{"--":<10}{"0":<10}')

while True:
    while True:
        opcao = int(input('Mostrar dados de qual jogador: '))

        if opcao <= len(jogadores):
            break

        else: 
            print('Jogador não encontrado... Tente outra vez!') 

    if opcao <= 0:
        break
    
    else:
        opcao -= 1

    print(f'-- Levantamento do jogador {jogadores[opcao]["nome"]}')
    for i in range(len(jogadores[opcao]['gols por partida'])):
        print(f'No jogo {i + 1}, fez {jogadores[opcao]["gols por partida"][i]}')