nome =input('qual eo seu nome?')
cod =int(input('qual eo codigo?'))
if nome == "admin" and cod == 999:
    print ("Acesso ao servidor liberado. Sistema online.")
else:
    print ("Falha na autenticação. Alerta de segurança ligado!")
    