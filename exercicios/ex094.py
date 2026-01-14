# Referente a aula015

# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# A média de idade do grupo.
# Uma listacom todas as mulheres.
# Uma lista com todas as pessoas com idade acima da média. 

dados = {}
pessoas = []
mulheres = []
idade_ac_media = []

while True:
    dados['nome'] = str(input('Nome: ')).strip()

    if dados['nome'] == '-': 
        break

    while True:
        dados['sexo'] = str(input('Sexo: ')).strip().lower()

        if dados['sexo'] in ('m', 'f'):
            break

        else:
            print('Valor incorreto... Tente novamente!')
    
    dados['idade'] = int(input('Idade: '))

    # Guardando os dados dessa pessoa em pessoas
    pessoas.append(dados.copy())

print(f'Pessoas cadastradas: {len(pessoas)}')

media_idade = sum(data['idade'] for data in pessoas) / len(pessoas)
print(f'Média de idade do grupo: {media_idade}')

for p in pessoas:
    if p['sexo'] in 'f': 
        mulheres.append(p)
    
    if p['idade'] > media_idade:
        idade_ac_media.append(p)

print('Mulheres: ')
for mulher in mulheres:
    print(f'    --> {mulher["nome"]}')

print('Pessoas com idade acima da média: ')
for acima_media in idade_ac_media:
    print(f'    --> {acima_media["nome"]}')
