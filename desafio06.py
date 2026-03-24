autorizados = ["Alice", "Bob", "Carlos"]
nome = input ("digite o nome de um pesquisador: ")


if nome in autorizados:
   indice = autorizados.index(nome)
   print(f"acesso permitido! o pesquisador {nome} esta na posição. ")

pergunta = input("deseja remover esse pesquisador da lista s/n: ")

if pergunta == "s":
        autorizados.remove(nome)
        print(f"lista autorizada {autorizados}")

else:
     print(f"acesso negado! o pesquisador {nome} nao foi encontrado")
     adicionar = input("deseja cadastrar esse novo pesquisador s/n: ")
     if adicionar == "s":
       autorizados.append(nome)
       print(f"lista atual{autorizados}")
