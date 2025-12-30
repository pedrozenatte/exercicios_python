# Referente a aula009

# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: 
# A média de idade do grupo.
# Qual é o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

nome = []
idade = []
sexo = []

for i in range(4):
     nome.append(str(input('Informe o nome {}: ' .format(i + 1))).strip())
     idade.append(int(input('Informe a idade {}: ' .format(i + 1))))
     sexo.append(str(input('Informe o sexo (Masculino ou Feminino) {}: ' .format(i + 1))).strip().lower())

soma = 0
posicao_mais_velho = 0
mais_velho = idade[0]
contador = 0

for i in range(4):
    # Somatório para a média
    soma += idade[i]
    # Encontro do maior
    if idade[i] > mais_velho and sexo[i][0] == 'm':
         mais_velho = idade[i]
         posicao_mais_velho = i
    if sexo[i][0] == 'f':
        if idade[i] < 20:
             contador += 1


# Média
media = soma / 4

print('Média: {}\nNome do mais velho: {}\nQntd de mulheres com menos de 20: {}' .format(media, nome[posicao_mais_velho], contador))
