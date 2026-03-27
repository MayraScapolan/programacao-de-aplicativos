compras = []
nome = ""
while nome != "fim":
    nome = input ("digite outro produto: ")
    if nome != "fim":
        compras.apeend(nome)


for p in compras:
    print(f"{p}")