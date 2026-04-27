def avaliar_desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"
    else:
        return "Insuficiente"


# Programa principal
try:
    nota_usuario = float(input("Digite a nota (0 a 10): "))
    
    if 0 <= nota_usuario <= 10:
        resultado = avaliar_desempenho(nota_usuario)
        print("Desempenho:", resultado)
    else:
        print("Por favor, digite uma nota válida entre 0 e 10.")
        
except ValueError:
    print("Entrada inválida. Digite um número.")