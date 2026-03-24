pendentes =["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
print(f"lista de pendentes {pendentes}")
concluidas = []

concluidas.append(pendentes[0])
pendentes.pop(0)

print("pendentes:" , pendentes)
print("concluidas" , concluidas)

