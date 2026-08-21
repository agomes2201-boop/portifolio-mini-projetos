soma = 0
media = 0
acimalimite = 0
for i in range(5):
    tempo = int(input("Digite o tempo em milisegundos: "))
    soma += tempo
    
    if tempo > 100:
        acimalimite += 1

media = soma / 5

print(f"Média dos tempos: {media} milisegundos")
print(f"Quantidade de tempos acima do limite: {acimalimite}")