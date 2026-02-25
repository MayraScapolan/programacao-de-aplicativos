valor_da_compra = float(input("digite o valor da compra:" ))
cupom = input("digite o cupom: ")
valor_do_cupom = 0.10

desconto = valor_da_compra * 0.10
novo_preco = valor_da_compra - desconto

if cupom == "DEV10":
    print("cupom aplicado com sucesso!" , novo_preco )
else:
    print("cupom  invalido:" , valor_da_compra)    
