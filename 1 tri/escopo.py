# Vida inicial do personagem
vida = 100

# Função para sofrer dano
def sofrer_dano(valor_dano):
    global vida
    vida -= valor_dano
    return vida

# Loop principal do jogo
while vida > 0:
    try:
        dano = int(input("Digite o dano causado pelo monstro: "))
        vida_atual = sofrer_dano(dano)
        print(f"Vida restante: {vida_atual}")
    except ValueError:
        print("Por favor, digite um número válido.")

# Quando a vida chega a 0 ou menos
print("Game Over")