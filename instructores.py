instructores=[]
seguir="s" 
while seguir=="s" or "S":
    menu=int(input("Ingrese la opción que va a ejecutar \n1. Insertar nombre de instructor \n2.Listar los instructores \n3.Modificar algún instructor \n4.Borrar un elemento de la lista \n5.Buscar instructor \n6.Ordenar la lista de forma ascendente \n"))
    if menu==1:
        instructores.append(input("Escriba el nombre del instructor que va a agregar \n"))
    elif menu==2:
        for i,e in enumerate(instructores):
           print("En la posición ",i," se encuentra ",e)
    elif menu==3:
        for i,e in enumerate(instructores):
            print("En la posición ",i," se encuentra ",e)
        a=int(input("Ingresa la posición del instructor que deseas modificar\n"))
        instructores[a]=input("Ingrese el nombre del instructor\n")
    elif menu==4:
        for i,e in enumerate(instructores):
            print("En la posición ",i," se encuentra ",e)
        p=int(input("Escriba la posicion del instructor que desea borrar: \n")) 
        del instructores[p]
    elif menu==5:
        Instructores1=[]
        for i in instructores:
            Instructores1.append(i.lower())
            Elemento=input("Ingrese el nombre del instructor que desea buscar: \n")
            print(" El instructor ingresado ",Elemento," se encuentra en la posición ",(Instructores1.index(Elemento)))
        
    elif menu==6:
        instructores.sort()
        for i,e in enumerate(instructores):
            print("En la posición ",i," se encuentra ",e)
        
    else:
        print("Opción invalida")
    seguir=input(" Escriba s o S para seguir en su lista \n")
    