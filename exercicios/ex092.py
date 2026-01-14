# Referente a aula015

# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionári. Se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar. 
# OBS: Para se aposentar, vamos considerar 35 anos de contribuição.

import datetime

dados = {}

dados['nome'] = str(input('Nome: ')).strip()
ano_nascimento = int(input('Ano de nascimento: ')) 
dados['idade'] = datetime.date.today().year - ano_nascimento
dados['carteira de trabalho'] = int(input('CTPS: '))

if dados['carteira de trabalho'] == 0:
    del dados['carteira de trabalho']

else:
    dados['ano de contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: '))

    tempo_aposentar = 35 - (datetime.date.today().year - dados['ano de contratacao'])
    
    dados['idade de aposentadoria'] = tempo_aposentar + dados['idade']

print('-' * 30)
print('DADOS' .center(30))
print('-' * 30)

print(f'Nome: {dados["nome"]}\nIdade: {dados["idade"]}')
if len(dados) == 6:
    print(f'CTPS: {dados["carteira de trabalho"]}\nAno de contratação: {dados["ano de contratacao"]}\nSalário: R${dados["salario"]:.2f}\nIdade de aposentadoria: {dados["idade de aposentadoria"]}')

print('-' * 30)
