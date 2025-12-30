# Referente a aula013

# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta. 


# Esse exercício foi resolvido pensando como um analisador sintático funciona

expressao = []
pilha = []
contador = 0

# frase = input('Expressao: ')
# expressao = list(frase)
expressao.extend(input('Expressão: '))

if '(' in expressao or ')'in expressao:
    for i in range(len(expressao)):
        if expressao[i] == '(':
            pilha.append(expressao[i])

        elif expressao[i] == ')':
            if not pilha: # Verifica se a pilha está vazia
                # Se está vazia, então tem parênteses que foi fechado sem ser aberto
                contador += 1 
                
            else:
                pilha.pop()

    if contador > 0 or pilha:
        if contador > 0: 
            print('Parênteses de fechamento foi encontrado sem um parênteses de abertura correspondente anterior.')

        if pilha: 
            print('Existem parênteses de abertura que nunca foram fechados') 

    else: 
        print('Expressão com parênteses correta!')

else: 
    print('Expressão não contém parênteses')