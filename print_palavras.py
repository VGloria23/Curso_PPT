arquivo = input('Digite o nome do arquivo: ')
total_palavras = []
arq_aberto = open(arquivo)
for linha in arq_aberto: # percorre linhas do arquivo que foi aberto
    linha = linha.strip() # remove espaco em branco
    palavras_na_linha = linha.split() # separa por espaco entre palavra
    for i in palavras_na_linha:
        if i not in total_palavras:
            total_palavras.append(i) # add
total_palavras.sort()
print(total_palavras)