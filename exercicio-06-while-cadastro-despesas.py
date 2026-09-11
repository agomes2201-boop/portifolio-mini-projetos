total_despesa = 0
quantidade_despesas = 0
maior_despesa = 0

while True:
    valor = float(input("Digite o valor da despesa (ou 0 para sair): "))
    
    if valor == 0:
        break
    
    quantidade_despesas += 1

    if valor > maior_despesa:
        maior_despesa = valor

    total_despesa += valor

print(f"Quantidade de despesas cadastradas: {quantidade_despesas}")
print(f"Maior despesa cadastrada: {maior_despesa}")
print(f"Total de despesas cadastradas: {total_despesa}")