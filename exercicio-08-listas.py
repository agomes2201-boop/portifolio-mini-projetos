estoque = [12, 3, 0, 8, 2]

total_unidades = 0
produtos_reposicao = []

for posicao, quantidade in enumerate(estoque, start=1):
    total_unidades += quantidade

    if quantidade < 5:
        produtos_reposicao.append(posicao)

print(f"Produtos para reposição: {produtos_reposicao}")
print(f"Total de unidades em estoque: {total_unidades}")
print(f"Total de produtos para reposição: {len(produtos_reposicao)}")