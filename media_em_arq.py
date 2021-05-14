nome = input("Digite o nome do arquivo: ") # nome do arquivo: mbox-short.txt 

arquivo = open(nome)
contador, soma = 0, 0

for linha in arquivo:
    if not linha.startswith("X-DSPAM-Confidence:") : continue # se a linha nao comeca assim, pula
    zero = linha.find('0') # acha o indice do primeiro 0 que aparecer
    num = linha[zero:] 
    num = float(num)
    contador += 1
    soma += num
media = soma / contador
print('Average spam confidence: ', media)