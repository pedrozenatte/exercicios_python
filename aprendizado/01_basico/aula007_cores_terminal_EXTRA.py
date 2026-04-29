# Aula 007 - Aula extra sobre Cores no Terminal

# ANSI - escape sequence

# Sempre que quiser representar uma cor em python, utilizar contrabarra:
# \033[style; text; back m
# Exemplo: \033[0; 33; 44m

# Style: Temos os códigos 0 (sem estilo), 1 (coloca o texto em negrito), 4 (sublinha o texto) e 7 (inverter as configurações)
# Text: Temos os códigos de 30 até 37 (30 - branco; 31 - vermelho; 32 - verde; 33 - amarelo; 34 - azul; 35 - roxo; 36 - ciano; 37 - cinza)
# Back: Temos de 40 até 47 (40 - branco; 41 vermelho... seguindo o mesmo padrão do text)

# --- PRÁTICA ----
print('\033[4;34;45mOlá, Mundo!\033[m') 
# OBS: O \033[m ao final, é para a faixa de cor ir só até o final do texto, ao invés de tudo.

