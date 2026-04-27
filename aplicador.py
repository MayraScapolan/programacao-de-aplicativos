def aplicar_promocao(precos):
    nova_lista = []
    
    for preco in precos:
        if preco > 100:
            desconto = preco * 0.15
            preco_final = preco - desconto
            nova_lista.append(preco_final)
        else:
            nova_lista.append(preco)
    
    return nova_lista


# Programa principal
compras = [150.0, 80.0, 200.0, 50.0]

compras_atualizadas = aplicar_promocao(compras)

print("Lista original:", compras)
print("Lista com desconto:", compras_atualizadas)