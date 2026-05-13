def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    # Lógica de aprovação
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao:
        return True
    else:
        return False


# Programa principal
nota = float(input("Digite a nota do teste: "))
xp = int(input("Digite os anos de experiência: "))
certificacao_input = input("Possui certificação? (s/n): ").lower()

# Converter para booleano
possui_certificacao = certificacao_input == 's'

# Chamada da função
aprovado = verificar_aprovacao(nota, xp, possui_certificacao)

# Resultado
if aprovado:
    print("Contratar")
else:
    print("Descartar")