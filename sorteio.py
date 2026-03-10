id = int(input("Qual o seu ID?: "))
compra = float(input("Qual o valor da compra?: "))

if id % 2 == 0 and compra > 500.0:
    print(f"Parabéns, usuário {id}! Você ganhou um cupom para sua compra de R$: {compra}.")
else:
    print(f"Obrigado pela compra, usuário {id}. Continue acompanhando nossas promoções!")