#01
def busca_sequencial(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1


vetor = [10, 25, 7, 42, 18, 30, 5, 60, 12, 9]

valor = 42
indice = busca_sequencial(vetor, valor)

print("1. Busca sequencial")
print("Índice encontrado:", indice)

#========================================================================================

#02
def contar_ocorrencias(lista, valor):
    contador = 0

    for elemento in lista:
        if elemento == valor:
            contador += 1

    return contador


lista = [5, 2, 5, 8, 5, 10, 3, 5]

print("\n2. Contagem de ocorrências")
print("O número 5 aparece", contar_ocorrencias(lista, 5), "vezes.")

#=========================================================================================

#03
def maior_e_posicao(vetor):
    maior = vetor[0]
    posicao = 0

    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
            posicao = i

    return maior, posicao


vetor = [15, 8, 32, 4, 27, 50, 12]

maior, posicao = maior_e_posicao(vetor)

print("\n3. Maior número")
print("Maior número:", maior)
print("Posição:", posicao)

#========================================================================================

#04
def buscar_aluno(alunos, nome):
    for aluno in alunos:
        if aluno == nome:
            return True

    return False


alunos = ["Luis", "Mavi", "Paulo", "Duda", "Mayra"]

nome = "Paulo"

print("\n4. Busca de aluno")

if buscar_aluno(alunos, nome):
    print(nome, "foi encontrado.")
else:
    print(nome, "não foi encontrado.")

#======================================================================================

#5
def primeira_ultima_posicao(vetor, valor):
    primeira = -1
    ultima = -1

    for i in range(len(vetor)):
        if vetor[i] == valor:
            if primeira == -1:
                primeira = i

            ultima = i

    return primeira, ultima


vetor = [3, 7, 5, 7, 9, 7, 2, 7, 10]

primeira, ultima = primeira_ultima_posicao(vetor, 7)

print("\n5. Primeira e última posição")
print("Primeira posição:", primeira)
print("Última posição:", ultima)

#======================================================================================