ataque = float(input("digite o poder do ataque do heroi"))
defesa = float(input("digite o poder da defesa do vilao"))

dano = ataque - defesa

if dano <= 0:
    print("o vilao bloqueou o ataque! dano:0")
elif dano > 0:
    print("ataque critico! você causou dano ao vilao de:" , dano )
   