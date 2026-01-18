# Referente a aula019

# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade. 

def leiaInt(frase: str = ''):

    """
    Lê um valor inteiro
    
    :param frase: String a ser impressa na tela.
    :type frase: str
    """

    while True:
        print(frase, end = '')
        numero = str(input()).strip()

        try:
            numero = int(numero)
            break
        
        except ValueError:
            print('Valor inválido... Tente outra vez')
         
    return numero

def leiaFloat(frase: str = ''):

    """
    Lê um valor float
    
    :param frase: String a ser impressa na tela
    :type frase: str
    """

    while True: 
        print(frase, end = '')
        numero = input().strip().replace(',', '.')

        try:
            numero = float(numero)
        
        except ValueError:
            print('Valor inválido... Tente outra vez!')

        else: 
            return numero
        

n = leiaInt('Int: ')
m = leiaFloat('Float: ')
print(f'Valores lidos: Int - {n} e Float - {m}')