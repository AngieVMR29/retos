def sumar(n1,n2):
    print("este es el método sumar")
    sumar=n1+n2
    return sumar
    

def restar(n1,n2):
    restar=n1-n2
    print("La resta entre el número 1 y el número 2 es ",restar)
    
def multiplicar( n1,n2):
    multiplicar=n1*n2
    return multiplicar

def dividir(n1,n2):
    dividir=n1/n2
    print("El resultado de la división es ",dividir)
    
def promedio():
    res=int(sumar(num1,num2))
    promedio=res/2
    print("El promedio de los números es ",promedio)
    
def sumarp():
    suma=0
    seguir="si"
    while seguir=="si":
        numero=int(input())
        suma=suma+numero
        seguir=input("Para seguir ingrese si de lo contrario no")
    return suma
    
print("Menú opciones")
num1=int(input("Ingrese el número 1: \n"))
num2=int(input("Ingrese el número 2: \n"))
op=input("Ingrese la o pción según la operación a realizar \n 1. Suma \n 2. Resta \n 3. Multiplicación \n 4. División \n 5. Promedio\n")
if op=="1":
    sumar()
elif op=="2":
    restar(num1,num2)
elif op=="3":
    multiplicar(num1,num2)
    print(f"La multiplicación entre {num1} y {num2} es {multiplicar(num1,num2)}")
    
elif op=="4":
    dividir(num1,num2)
    
elif op=="5":
    promedio()
    
