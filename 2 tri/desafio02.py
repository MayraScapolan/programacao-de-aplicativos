def criar_arquivo():
    open('habitos.txt' , 'w').close()
criar_araquivo()


def cadastra_habito():
    inserir = input("Digite seu novo abito: ")
    with open('habitos.txt' , 'a') as m:
        m.write(destino + '\n')
    print("")
