def calcula_viagem(distancia, consumo, preco_combustivel):
    """
    Calcula o custo total de uma viagem.

    Parâmetros:
    distancia (float): A distância da viagem em quilômetros.
    consumo (float): O consumo do veículo em km/l.
    preco_combustivel (float): O preço do combustível por litro.

    Retorna:
    float: O custo total da viagem.
    """
    litros_necessarios = distancia / consumo
    custo_total = litros_necessarios * preco_combustivel
    return litros_necessarios, custo_total

distancia = float(input("Digite a distância da viagem em quilômetros: "))
consumo = float(input("Digite o consumo do veículo em km/l: ")) 
preco_combustivel = float(input("Digite o preço do combustível por litro: "))

resultado = calcula_viagem(distancia, consumo, preco_combustivel)

print(f"Litros necessários para a viagem: {resultado[0]:.2f} litros")
print(f"Custo total da viagem: R$ {resultado[1]:.2f}")