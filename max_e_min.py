cont, soma, maximo, minimo = 0, 0, None, None

while True:
    try:
        entrada = input('Digite um número: ')
        if entrada == 'pronto':
            break     
        entrada = int(entrada)
        soma += entrada
        cont += 1
        if maximo == None or entrada > maximo:
            maximo = entrada
        if minimo == None or entrada < minimo:
            minimo = entrada
    except:
        print('Entrada inválida')
        continue
print(soma, cont, maximo, minimo)