# Referente a aula012

# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular. 

tupla = (
    'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
    'Estojo', 25.0, 'Transferidor', 4.20, 'Compasso', 9.99,
    'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90    
    )

print('-' * 60)
print('LISTAGEM DE PREÇOS' .center(60))
print('-' * 60)

for i in tupla:
    # if type(i) == (float) or type(i) == (int):
    # Essa comparação apesar de semanticamente correta, não é boa prática utilizá-la, primeiro, pois ela não carrega herança, ou seja, o valor de "i" necessariamente precisa ser INTEIRO ou FLOAT, e não basta apenas se comportar como float, e a forma abaixo é mais limpa, uma vez que aceita mais de um tipo
    if isinstance(i, (int, float)):
        print(f'R${i:>7.2f}')
    
    else: 
        print(f'{i:.<50}', end = '')

    
