# Módulo de cadastro

# OBS: Em linguagem C, normalmente faziamos funções para abrir e fechar o arquivo corretamente, mas aqui em Python não tem essa necessidade, pois a segurança de abrir e fechar corretamente está embutido em estruturas como with. 

import os


# Função para deletar o arquivo
def deletarArquivo():
    
    """
    Deleta o arquivo cadastro.py
    """
    
    if os.path.exists('/home/pedro/exercicios_python/exercicios/ex115/arquivos/cadastro.txt'):
        os.remove('/home/pedro/exercicios_python/exercicios/ex115/arquivos/cadastro.txt')


# Função para criar ou apagar tudo que estiver no arquivo
def criaArquivo():
    
    """
    Cria o arquivo ou apaga todos os dados existentes nele.
    """

    open('/home/pedro/exercicios_python/exercicios/ex115/arquivos/cadastro.txt', 'w').close()


# Função para verificar a existência de um arquivo
def existeArquivo():
    pass


# Função para ler arquivo
def lerArquivo():

    """
    Lê as pessoas cadastradas
    """

    try: 
        with open('/home/pedro/exercicios_python/exercicios/ex115/arquivos/cadastro.txt', 'r') as file:
            return file.read()
    
    except FileNotFoundError:
        print('Erro ao abrir o arquivo para a leitura. Arquivo inexistente.')


# Função para cadastrar uma pessoa
def cadastrar(nome: str = '<desconhecido>', idade: int = 0):
    
    """
    Cadastra uma pessoa no arquivo cadastro.txt
    
    :param nome: Nome da pessoa
    :type nome: str
    :param idade: Idade da pessoa
    :type idade: int
    """

    try:
        with open('/home/pedro/exercicios_python/exercicios/ex115/arquivos/cadastro.txt', 'a') as file:
            file.write(f'{nome:<20}{idade:<3}anos\n')
    
    except FileNotFoundError:
        print('Erro ao abrir o arquivo para a escrita. Arquivo inexistente.')



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