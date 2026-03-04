nome = input("digite o teu nome: ")
usuario = input("qual o teu usuario?: ")
senha = int(input("digite a senha: "))

if (usuario == "admins" or usuario == "root") and senha == 12345:
    print("acesso liberado!")

else:
    print("acesso negado!")