# 1. Definição da função eh_par
def eh_par(numero):
    """
    Verifica se um número é par.
    Retorna True se for par, False se for ímpar.
    """
    # Um número é par se o resto da divisão por 2 for 0
    return numero % 2 == 0

# 2. Programa Principal
# Solicita o número ao usuário e converte para inteiro
try:
    num = int(input("Digite um número: "))

    # 3. Chama a função e exibe o resultado
    if eh_par(num):
        print("Este número é par")
    else:
        print("Este número é ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")