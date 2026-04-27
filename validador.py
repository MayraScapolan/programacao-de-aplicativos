def senha_valida(senha):
    return len(senha) >= 6


# Programa principal
while True:
    senha = input("Digite uma senha: ")
    
    if senha_valida(senha):
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("A senha deve ter pelo menos 6 caracteres. Tente novamente.")