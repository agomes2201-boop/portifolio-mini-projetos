def calcular_duracao(duracao, veloc_rep):
    calculo = duracao / veloc_rep
    minutos = int(calculo)
    segundos = (calculo - minutos) * 60
    return minutos, segundos

minutos, segundos = calcular_duracao(120, 2)
print(f"Duração: {minutos} minutos e {segundos:.2f} segundos")