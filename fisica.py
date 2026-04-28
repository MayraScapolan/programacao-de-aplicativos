# Função para converter km/h para m/s
def converter_km_para_ms(velocidade_kmh):
    return velocidade_kmh / 3.6

# Programa principal
try:
    velocidade = float(input("Digite a velocidade em km/h: "))

    if velocidade > 80:
        velocidade_ms = converter_km_para_ms(velocidade)
        print(f"Velocidade em m/s: {velocidade_ms:.2f}")
        print("Reduza a velocidade!")
    else:
        print("Velocidade dentro do limite.")

except ValueError:
    print("Por favor, digite um número válido.")