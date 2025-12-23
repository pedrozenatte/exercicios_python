# Referente a aula012

# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

contagem = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
    'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
    'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze',
    'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte'
)

while True:
    pos = int(input('Escreva um valor de 0 a 20: '))
    
    if pos < 0 or pos > 20:
        print('Valor inválido... Tente outra vez')
    
    else:
        break

print(contagem[pos])