cargo = input("qual o teu cargo?: ")
cod_acesso = int(input("digite o codigo de acesso: "))
botao_de_emergencia = input("o botao de emergencia foi pressionado? S/N: ")
equipamentos = input ("voce esta com o epi completo S/N: ")

if cargo == "engenheiro" or (cargo == "tecnico" and cod_acesso == 1234) or (botao_de_emergencia == "S" and equipamentos == "S"):
    print("acesso autorizado!")

else:
    print("acesso negado: RISCO DE SEGURANÇA")   