# Referente a aula015

# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela. 

aluno = {}
alunos = []

# Condição de parada: '-' 
while True:
    aluno['nome'] = input('Nome: ').strip()

    if aluno['nome'] == '-':
        break

    aluno['nota'] = float(input(f'Média de {aluno["nome"]}: '))

    if aluno['nota'] < 5:
        aluno['situacao'] = 'Reprovado'
    
    else: 
        aluno['situacao'] = 'Aprovado'

    alunos.append(aluno.copy())

print('-' * 30)
print('Lista' .center(30))
print('-' * 30)
print(f'{"Nome":<10}{"Nota":<10}{"Situação":<10}\n')

for a in alunos: # Cada 'a' é um item da lista, sendo que cada item é um dicionário
    print(f'{a["nome"]:<10}{a["nota"]:<10}{a["situacao"]:<10}')
