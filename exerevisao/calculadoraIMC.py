peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc > 25:
    print("você esta acima do peso.")
else:
    print("você está abaixo do peso.")

9
bjetos = ["Faca", "Tesoura", "Colher", "Garfo"]

while len(objetos) > 0:
    retirado = objetos.pop(0)
    print(f"objetos removidos", objetos)

