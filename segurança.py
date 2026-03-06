seguranca = input("voce concluiu o curso de segurança? s/n: ")

if seguranca == "s":
    instrutor = input("o instrutor esta na sala? s/n: ")
    if instrutor == "s":
        print("acesso liberado! operação iniciada.")
    else:
        print("aguarde o instrutor para ligar a maquina.")   

else:
    print("acesso negado! Faça o treinamento primeiro.")