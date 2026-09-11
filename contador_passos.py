numeros = list(range(1, 101))

def busca_sequencial(lista, alvo):
    comparacoes = 0

    for i in range(len(lista)):
        comparacoes += 1

        if lista[i] == alvo:
            print("Busca Sequencial:")
            print("Número encontrado na posição:", i)
            print("Quantidade de comparações:", comparacoes)
            return i

    print("Número não encontrado.")
    print("Quantidade de comparações:", comparacoes)
    return -1


def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == alvo:
            print("\nBusca Binária:")
            print("Número encontrado na posição:", meio)
            print("Quantidade de comparações:", comparacoes)
            return meio

        elif lista[meio] < alvo:
            inicio = meio + 1

        else:
            fim = meio - 1

    print("Número não encontrado.")
    print("Quantidade de comparações:", comparacoes)
    return -1


busca_sequencial(numeros, 95)
busca_binaria(numeros, 95)
