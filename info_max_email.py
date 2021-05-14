arquivo = input('Digite o nome do arquivo: ')
abre_arquivo = open(arquivo)
emails = dict()

for linha in abre_arquivo:
    if not linha.startswith('From '): continue
    linha = linha.strip() # remove espaco em branco
    linha = linha.split()
    emails[linha[1]] = emails.get(linha[1], 0) + 1

pessoa, maximo = None, None
for remetente, quant in emails.items():
    if pessoa == None or quant > maximo:
        pessoa = remetente
        maximo = quant

print(pessoa, maximo)