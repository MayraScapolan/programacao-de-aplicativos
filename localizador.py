cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
tarefa = input ("digite o nome de uma cidade")

if tarefa in cidades:
    posicao = cidades.index(tarefa)
    print(f"a cidade {tarefa} esta na posicao {posicao}")
else:
    print(f"a {tarefa} nao foi encontrada")

