# Referente a aula012

# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais. 

palavras = ('Alface', 'Abacate', 'Laranja', 'Banana', 'Morango')

for item in palavras:
    print(f'As vogais da palavra {item} são: ', end = '') 

    if item.lower().count('a') > 0:
        print('a ', end = '')
    
    if item.lower().count('e') > 0:
        print('e ', end = '')

    if item.lower().count('i') > 0:
        print('i ', end = '')

    if item.lower().count('o') > 0:
        print('o ', end = '')

    if item.lower().count('u') > 0:
        print('u ', end = '')
    
    print()

