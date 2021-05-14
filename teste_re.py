import re

soma = 0
arq = input()
arq_aberto = open(arq)
for linha in arq_aberto:
    linha = linha.strip()
    numero = re.findall('\S([0-9]+)\S', linha)
    numero = int(numero)
    soma += numero

print(numero)