
import os

sexoiden={1:"varon",2:"mujer"}
tupla=("Posadas","Garupa","Candelaria")


def limpiar():
    os.system("cls")


def lectura():
    archivo=open("empleados.txt","r")
    lista=archivo.readline()
    empleado={}
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        indice=int(lineas[0])
        nombre=lineas[1]
        sexo=int(lineas[2])
        sueldo=float(lineas[3])
        sucursal=int(lineas[4])
        empleado[indice]=nombre,sexo,sueldo,sucursal
        lista=archivo.readline()
    archivo.close()
    return empleado

    
def comprobacion(parametro):
    lista=lectura()
    for indice in lista:
        if parametro!=indice:
            return True
        if parametro==indice:
            print("Clave ya existe. Sólo puede modificar o borrar")
            return False

def por_sucursal(parametro):
    lista=lectura()
    limpiar()
    cont=0
    print("Listado por sucursal: \n")
    for indice in lista:
        if lista[indice][3]==1:
            sucursal=tupla[0]
        if lista[indice][3]==2:
            sucursal=tupla[1]
        if lista[indice][3]==3:
            sucursal=tupla[2]
        if lista[indice][3]==parametro:
            print("Sucursal:",sucursal,":\n")
            print("dni: ",indice,"\nnombre y apellido: ",lista[indice][0],"\nsexo: ",sexoiden[lista[indice][1]],"\nsueldo: $",lista[indice][2])
            print("-----------------------------------------------")
            cont=cont+1
    if cont==0:
        print("Aun no hay empleados listados en la sucursal")  

def por_dni(parametro):
    lista=lectura()
    limpiar()
    cont=0
    print("Listado por D.N.I: \n")
    for indice in lista:
        if indice==parametro:
            if lista[indice][3]==1:
                sucursal=tupla[0]
            if lista[indice][3]==2:
                sucursal=tupla[1]
            if lista[indice][3]==3:
                sucursal=tupla[2]
            print("DNI: ",indice)
            print("\nnombre y apellido: ",lista[indice][0],"\nsexo: ",sexoiden[lista[indice][1]],"\nsueldo: $",lista[indice][2],"\nSucursal: ",sucursal)
            print("-----------------------------------------------")
            cont=cont+1
        if cont==0:
            print("Aun no hay empleados listados en la sucursal")
    