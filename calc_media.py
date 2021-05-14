cont, soma, media = 0, 0, 0
while True:
    try:
        entrada = input('Digite um número: ')
        if entrada == 'pronto':
            break     
        entrada = int(entrada)
        soma += entrada
        cont += 1
        media = soma / cont
    except:
        print('Entrada inválida')
        continue
    
print(soma, cont, media)