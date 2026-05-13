idade =int(input("qual a sua idade? " ))
ingresso = input ("possui ingresso? (s/n) ")
lista = input ("esta na lista? (s/n) ")

if idade >= 18 and ingresso == "s" or lista == "s":
   print("acesso permitido") 
elif idade < 18 and ingresso  == "n" or lista == "n":
  print("acesso negado")