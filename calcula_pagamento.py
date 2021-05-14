def calculo_pagamento(hora, taxa_hora):
    if hora > 40:
        base = 40 * taxa_hora
        extra = (hora - 40) * 1.5 * taxa_hora
        pagamento = base + extra
    else:
        pagamento = 40 * taxa_hora
    return pagamento

h = int(input('Insira as horas: '))
taxa = int(input('Insira o valor da hora de trabalho: '))
resp = calculo_pagamento(h, taxa)
print('Pagamento:', resp)