# Função para somar os valores do carrinho
def somar_carrinho(precos):
    total = sum(precos)
    
    if total > 500:
        total *= 0.9  # aplica 10% de desconto
    
    return total

# Programa principal
carrinho = [150.0, 200.0, 180.0, 50.0]

valor_final = somar_carrinho(carrinho)

print(f"Valor final a pagar: R$ {valor_final:.2f}")