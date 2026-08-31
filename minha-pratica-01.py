num_1 = int(input("Digite o primeiro número: "))
num_2 = int(input("Digite o segundo número: "))

resultado = divmod(num_1, num_2)
print(f"Resultado da divisão: {resultado[0]} e o resto é: {resultado[1]}")