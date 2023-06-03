personalizada=int(input("Ingrese 1 si su tarjeta está personalizada o 2 si no esta personalizada: \n"))

if personalizada==1:
    transbordo=int(input("Usted está realizando transbordo, ingrese 1 para si o 2 para no: \n"))
    if transbordo==1:
        print("¡Tranferencia realizada!")
    elif transbordo==2:
        recargaDisponible=int(input("Ingrese la recarga que tiene disponible: \n"))
        if recargaDisponible>2950:
            saldo=recargaDisponible-2950
            print("El saldo que le queda es ",saldo)
        elif recargaDisponible<2950 and recargaDisponible>0:
            saldo=recargaDisponible-2950
            print("No olvide recargar antes de la siguiente subida, usted debe",saldo)
        elif recargaDisponible<0:
            print("¡Saldo insuficiente!")
        else:
            print("¡Tarejta invalida!")
    else:
        print("¡Error!")
elif personalizada==2:
    recargaDisponible=int(input("Ingrese la recarga que tiene disponible: \n"))
    if recargaDisponible>2950:
        saldo=recargaDisponible-2950
        print("El saldo que le queda es ",saldo)
    elif recargaDisponible<2950:
        print("¡Saldo insuficiente!")
else:
    print("¡Tarejta invalida!")
