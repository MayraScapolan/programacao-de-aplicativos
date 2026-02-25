temperatura = float(input("digite a temperatura do servidor:" ))

if temperatura >= 80:
    print("PERIGO! desligue o servidor por superaquecimento")
elif temperatura >= 50 < 80:
    print("Alerta: Ventoinhas ligadas no máximo!")
elif temperatura < 50:
    print("Temperatura estável. Sistema operando normalmente.")
    