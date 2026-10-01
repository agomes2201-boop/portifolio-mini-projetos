indisponibilidade = float(input("Digite a quantidade de minutos de indisponibilidade do servidor:"))
incidentes = int(input("Digite a quantidade de incidentes ocorridos no servidor:"))

if indisponibilidade < 0 or incidentes < 0:
    print("Valores inválidos inseridos.")
elif indisponibilidade <= 30 and incidentes == 0:
    print("SLA Cumprido: O servidor está dentro do SLA.")
elif indisponibilidade <= 60 and incidentes <= 1:
    print("Atenção")
else:
    print("SLA Não Cumprido: O servidor está fora do SLA.")