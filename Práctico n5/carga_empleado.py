import os
def limpiar():
    os.system("cls")

def titulo_subrayado(titulo,caracter="-"):
    print(titulo)
    print(caracter*len(titulo))


def continuar(f1,f2,f3,f4):
    archivo=open("empleado.txt","r")
    contador=0
    lista=archivo.readline()
    while lista!="":
        contador=contador+1
        lista=archivo.readline()
    archivo.close
    archivo=open("empleado.txt","a")
    for x in range(cont):
        contador=contador+1
        archivo.write(str(contador))
        archivo.write(",")
        archivo.write(f2[x])
        archivo.write(",")
        archivo.write(str(f3[x]))
        archivo.write(",")
        archivo.write(str(f4[x]))
        archivo.write("\n")
    archivo.close
def seleccion():
    comp=0
    while comp!=0:
        try:
            op=int(input("1-crear un archivo nuevo: \n2-continuar agregando:\nopcion: "))
            if op==1:
                archivo=open("empleado.txt","w")
                archivo.close
                break
            if op==2:
                archivo=open("empleado.txt","r")
                archivo.close
                break
            else:
                print("la opcion no es la correcta: ")
                op=int(input("1-crear un archivo nuevo: \n2-continuar agregando:\nopcion: "))
        except:
            print("la obcion no es la correcta")
    limpiar()

#bloque principal

codigo=[]
empleado=[]
sueldo=[]
categoria=[]
cont=0
op=1

while op!=2:
    titulo_subrayado("      BIENVENIDOS AL PROGRAMA DE CARGA DE DATOS")
    cont=cont+1
    codigo.append(cont)
    valor1=input("ingrese el nombre del empleado: ")
    empleado.append(valor1)
    valor2=float(input("ingrese el sueldo del empleado: "))
    sueldo.append(valor2)
    valor3=0
    while valor3>2 or valor3<1:
        try:
            valor3=int(input("ingresar un \n1 si es mecanico \n 2 si es conductor\nopcion:  "))
            if valor3>2 or valor3<1:
                print("ERROR AL INGRESAR EL DATO: ")
        except:
            print("ERROR\n Ingrese nuevamenete los datos:\n ") 
    categoria.append(valor3)
    op=int(input("desea seguir con la carga digite si=1  no=2: "))
    try:
        if op==2:
            limpiar()
        if op==1:
            limpiar()
    except:
        print("ERROR AL INGRESAR EL DATO")


#bloque principal

titulo_subrayado("      BIENVENIDOS AL PROGRAMA DE CARGA     ")
continuar(codigo,empleado,sueldo,categoria)
limpiar()
titulo_subrayado("      FIN DE LA CARGA        ")
