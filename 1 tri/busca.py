def esta_na_lista(lista, nome_busca):
    for item in lista:
        if item == nome_busca:
            return "Encontrado!"
    return "Não disponível"


# Programa principal
frutas = ["maçã", "banana", "laranja", "uva"]

busca = input("Digite o nome para buscar: ")

resultado = esta_na_lista(frutas, busca)

print("Resultado da busca:", resultado)