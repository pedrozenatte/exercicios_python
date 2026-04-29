# Utilizando Módulos

# São as bibliotecas em python
# import biblioteca

# Porém, se quiser limitar a biblioteca, podemos utilizar:
# from biblioteca import 'tal coisa'


# Biblioteca math:
# ceil --> Arredonda para cima
# floor --> Arredonda para baixo
# trunc --> Faz um truncamento (elimina da vírgula para frente, sem fazer arredondamento)
# pow --> Potência
# sqrt --> Raíz
# factorial --> Fatorial de um número

#import math
from math import sqrt, floor # Para aparecer todas as funções da biblioteca, basta apertar Ctrl + Espaço

num = int(input('Digite um número: '))
#raiz = math.sqrt(num)
# OBS: Sempre que escrever o nome da biblioteca e o ponto, por exemplo, math. --> é para aparecer TODAS as funções caso tenha sido importada a biblioteca toda. 

# Se foi importata apenas a função específica da biblioteca, como no caso de from math import sqrt, utilizar a função diretamente:
raiz = sqrt(num)

print('A raiz de {} é igual a {:.3f}' .format(num, floor(raiz)))

# Bibliotecas por padrão
# ATENÇÃO: Vá em python.org --> Doc --> Library Reference, lá você encontra todas as bilbiotecas básicas que vem com o python por padrão
# Exemplo, ir no Numeric and Mathematical Modules

import random 

num2 = random.randint(1, 10)

print(num2)


# Bibliotecas que podem ser importadas separadamente
# ATENÇÃO: Vá em python.org --> Pypi (esse é o index de pacotes extras, criadas pela comunidade)
# Essas bibliotecas não estão no python padrão, então precisam ser baixadas --> Veja o manual da instalação pela biblioteca, por exemplo: python -m pip install emoji --upgrade
