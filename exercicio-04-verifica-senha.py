senha = input("Digite sua senha: ")

tem_maiuscula = False
tem_numero = False

for caractere in senha:
    if caractere.isupper():
        tem_maiuscula = True 
    if caractere.isdigit():
        tem_numero = True

tamanho_valido = len(senha) >= 8

if tem_maiuscula and tem_numero and tamanho_valido:
    print("Senha válida!")
else:
    print("Senha inválida! A senha deve ter pelo menos 8 caracteres, incluir pelo menos uma letra maiúscula e um número.")