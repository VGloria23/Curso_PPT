arquivo = input('Digite o nome do arquivo: ')
arq_aberto = open(arquivo)
cont = 0

for linha in arq_aberto:
    linha = linha.strip()
    remetente = linha.split()
    if linha.startswith('From '):
        print(remetente[1])
        cont += 1
print('There were {} lines in the file with From as the first word'.format(cont))