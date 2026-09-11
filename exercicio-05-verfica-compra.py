valor_compra = float(input("Digite o valor da compra: "))
forma_pagamento = input("Digite a forma de pagamento (dinheiro, cartão ou pix): ").lower()


if valor_compra >= 300:
    desconto = 0.10
elif valor_compra >= 150:
    desconto = 0.05
else:
    desconto = 0.0

total = valor_compra * (1 - desconto)

if forma_pagamento == "pix":
    total = total - (total * 0.02)

print(f"Valor da compra: R$ {total:.2f}")
