vagas = ["ocupado", "livre", "ocupado", "livre"]
vagas = int (input("digite o numero de uma vaga (0 a 3)"))

if vagas % 2 == 0 or vagas == "livres":
    print(f"vagas {indice} autorizada para estacionar.")
else:
    print(f"vagas{indice} indisponivel ou fora das regras.")
