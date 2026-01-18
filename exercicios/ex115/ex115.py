# Referente a aula019

# Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: Cadastrar uma nova pessoa e listar todas as pessoas cadastradas. 

import cadastrar 

while True:
    print('=' * 30)
    print('MENU PRINCIPAL' .center(30))
    print('=' * 30)
    print('1 - Ver pessoas cadastradas\n2 - Cadastrar nova Pessoa\n3 - Sair do sistema')

    opcao = cadastrar.leiaInt('Sua opção: ')

    if opcao == 1: 
        dados = cadastrar.lerArquivo()

        print('=' * 30)
        print('PESSOAS CADASTRADAS' .center(30))
        print('=' * 30)
        print(cadastrar.lerArquivo(), end = '')
        print('-' * 30)
    
    elif opcao == 2:
        while True:
            try: 
                cadastrar.cadastrar(str(input('Nome: ')).strip(), int(input('Idade: ')))
                break

            except (TypeError, ValueError):
                print('Idade inválida... Tente outra vez!')

    elif opcao == 3:
        break

    else: 
        print('Opção inválida... Tente outra vez!')


 

