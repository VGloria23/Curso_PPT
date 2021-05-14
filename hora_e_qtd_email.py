arquivo = input('Digite o nome do arquivo: ') # o nome do arquivo eh mbox-short.txt
abre_arquivo = open(arquivo)
horas = dict()

for linha in abre_arquivo:
    if not linha.startswith('From '): continue # pula caso a linha nao comece com 'From'
    linha = linha.strip() # remove espaco em branco
    linha = linha.split() # separa por espaço
    horario_cravado = linha[5]
    limite = horario_cravado.find(':')
    horas[horario_cravado[:limite]] = horas.get(horario_cravado[:limite], 0) + 1

ordenada = sorted(horas.items())
for hora, quant in ordenada:
    print(hora, quant)