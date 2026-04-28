# Função para contar caracteres
def contar_caracteres(texto):
    return len(texto)

# Programa principal
usuario = input("Digite um nome de usuário: ")

tamanho = contar_caracteres(usuario)

if tamanho < 5:
    print("Nome de usuário muito curto")
else:
    print("Nome aceito")