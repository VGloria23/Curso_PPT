def computar_notas(n):
    try:
        if n >= 0.9 and n <= 1:
            nota = 'A'
        elif n >= 0.8 and n < 0.9:
            nota = 'B'
        elif n >= 0.7 and n < 0.8:
            nota = 'C'
        elif n >= 0.6 and n < 0.7:
            nota = 'D'
        elif n < 0.6:
            nota = 'F'
        print(nota)
    except:
        print('Pontuação inválida')

nota = float(input('Insira a pontuação: ')) 
computar_notas(nota)       