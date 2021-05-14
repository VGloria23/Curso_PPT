entrada = input('Digite uma palavra: ')

tamanho = -len(entrada)  #indice negativo = começar pelo ultimo indice
letra = -1

while letra >= tamanho:
    print(entrada[letra])
    letra -= 1