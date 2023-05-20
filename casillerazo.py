seguir="Si"
apostar=0
valorglobal=10000

from random import randint
def lanzarmoneda():
    nombreJugador=input("Ingrese su nombre: \n")
    Moneda= randint(1,2)
    return (nombreJugador,Moneda)

def jugar():
    eleccion=int(input("Escoja 1 para cara o 2 para sello\n"))
    apostado=int(input("Ingrese valor a apostar\n"))
    return (eleccion,apostado)

def ganar(valorglobal,apos):
  
    apostar=apos*2
    valorglobal=valorglobal+apostar
    print("Su ganancia es de ",apos," y el valor para apostar que le queda es de ",valorglobal)
    
    
def perder(valorglobal,apos):
    valorglobal=valorglobal-apos
    print("Su perdida es de ",apos," y el valor para apostar que le queda es de ",valorglobal)

    
while seguir=="Si" or seguir=="si" or seguir=="sI" or seguir=="SI":
    
    nombreJugador,moneda=lanzarmoneda()
    eleccion,apo=jugar()
    if moneda==1 and eleccion==1:
        print("Salió cara y usted escogió cara ¡Ganaste,",nombreJugador,"!")
        ganar(valorglobal,apo)
        seguir=input("¿Desea seguir jugando?\n")
    elif moneda==2 and eleccion==2:
        print("Salió sello y usted escogió sello ¡Ganaste,",nombreJugador,"!")
        ganar(valorglobal,apo)
        seguir=input("¿Desea seguir jugando?\n")
    elif moneda==1 and eleccion==2:
        print("Salió cara y usted escogió sello ¡Perdiste, ",nombreJugador," !")
        perder(valorglobal,apo)
        seguir=input("¿Desea seguir jugando?\n")
    elif moneda==2 and eleccion==1:
        print("Salió sello y usted escogió cara ¡Perdiste, ",nombreJugador,"!")
        perder(valorglobal,apo)
        seguir=input("¿Desea seguir jugando?\n")
    elif moneda!=2 or eleccion!=1:
        print("Digitaste una opción invalida")
    else:
        print("Datos incorrectos")
        
        
