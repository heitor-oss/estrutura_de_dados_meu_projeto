def gerar_ponto():
    return (1, 2, 4)
ponto = gerar_ponto()
print(type(ponto))
primeiro, *final = ponto # desempacotamento
print(primeiro)
print(final)


