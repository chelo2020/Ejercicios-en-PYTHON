#Ejercicio 1: Ingresar por teclado los 
#siguientes datos y grabar en un archivo plano (empleado.dat)
#Codigo Empleado, Nombre Y Apellido, Edad, Sexo, Estado Civil
#Valores en campos:    Sexo: 1 = varón, 2 = mujer.

#Estado Civil: 1 = soltero, 2 = casado.
 #Informar:

#a.Cantidad de empleados.
#b.Cantidad de varones.
#c.Cantidad de mujeres solteras.
#Ejercicio 2: Teniendo en cuenta los datos Ingresados en el archivo (empleado.dat),
#
# Obtener una planilla según diseño, ordenado alfabéticamente.
#------------------------------------------
#Cód. Empl.
#Nombre y Apellido
#Edad
#Sexo
#Total de Empledos
#--------------------------------------------
#a.Cantidad de mujeres entre 20 y 30 años.
#b.Cantidad de mujeres casadas entre 30 y 40 años.
#c.Cantidad de mujeres casadas.
#3.Total de varones.
#e.Total de varones solteros con edad de 25 años.
#f.Total de varones casados.

#NOTA: La columna “Observaciones” deberá escribir la palabra  ‘Varón’  si el valor del campo  
# “Sexo” es igual a 1 y,  ‘Mujer’ si el valor de “Sexo” es 2

def bienvenida():
    print("                                 BIENVENIDOS AL SISTEMA DE CARGA DE EMPLEADOS:")
    print("")
    print("")

import os
def limpiar():#defino una variable para limpiar la pantalla
    os.system("cls")

def lec_o_esc():#funcion opcional para crear archivo o escribir en uno preexistente
    comp=0
    while comp==0:
        try:
            print("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente: ")
            op=int(input("opcion: "))
            if op==1:
                arch=open("archivo.txt","w")
                comp=1
                break
            if op==2:
                arch=open("archivo.txt","r")
                comp=1
                break
            if op<1 or op>2:
                print("ERROR,  el valor ingresado no es correcto")
        except:
            print("EL VALOR INGRESADO NO ES CORRECTO INGRESE NUEVAMENTE")    
    arch.close()
    limpiar()


def archivo(v1,v2,v3,v4,v5):#funcion para escribir el archivo
    arch=open("archivo.txt","r")#cuento la cantidad de lineas que tiene el archivo
    lista=arch.readline()
    contl=0#utilizo un contador de referencia para cargar el codigo de empleado
    while lista!="":
        contl=contl+1
        lista=arch.readline()
    arch.close()
    arch=open("archivo.txt","a")
    for x in range(cont):
        contl=contl+1
        arch.write(str(contl))#utilizo el contador para agregar el valor a la siguiente carga
        arch.write(",")
        arch.write(v2[x])
        arch.write(",")
        arch.write(str(v3[x]))
        arch.write(",")
        arch.write(str(v4[x]))
        arch.write(",")
        arch.write(str(v5[x]))
        arch.write("\n")
    arch.close()



#//////////////////////////////////////PROGRAMA////////////////////////////////////
cont=0#total de empleados
codemp=[]#codigo empleado
nom=[]#nombre y apellido del empleado
edad=[]#edad del empleado
sexo=[]#sexo del empleado
ecivil=[]#estado civil
opcion=1#variable para consultar las veces de la carga
limpiar()
bienvenida()
lec_o_esc()#invoco la funcion para crear o continuar escribiendo al archivo (archivo.txt)

while opcion!=0:
    bienvenida()
    cont=cont+1
    lista1=cont
    codemp.append(lista1)
    lista2=input("ingrese el nombre del empleado: ")
    nom.append(lista2)
    comp=0
    while comp==0:
        try:
            lista3=int(input("ingrese la edad del empleado: "))
            edad.append(lista3)
            comp=1
        except:
            print("error: ingrese nuevamente:")
    comp=0
    while comp==0:
        try:
            print("Ingrese el sexo del empleado \n(-1-si es masculino), (-2-si es femenino)")
            lista4=int(input("opcion: "))
            if lista4==1 or lista4==2:
                comp=1
            if lista4>2:
                print("EL VALOR INGRESADO NO ES CORRECTO")
                lista4=int(input("INGRESE NUEVAMENTE:"))
            if lista4<1:
                print("EL VALOR INGRESADO NO ES CORRECTO")
                lista4=int(input("INGRESE NUEVAMENTE:"))
        except:
            print("error: ingrese nuevamente:")
    sexo.append(lista4)
    comp=0
    while comp==0:
        try:
            print("Ingrese el estado civil:\n-1) SOLTERO\n-2) CASADO")
            lista5=int(input("opcion: "))
            if lista5==1 or lista5==2:
                comp=1
            if lista5>2:
                print("EL VALOR INGRESADO NO ES CORRECTO")
                lista5=int(input("INGRESE NUEVAMENTE:"))
            if lista5<1:
                print("EL VALOR INGRESADO NO ES CORRECTO")
                lista5=int(input("INGRESE NUEVAMENTE:"))
        except:
            print("EL VALOR INGRESADO NO ES CORRECTO")
    ecivil.append(lista5)

    comp=0
    while comp==0:
        try:    
            opcion=int(input("Desea continuar? 1)-si  0)-no: "))
            if opcion==1:
                comp=1
            if opcion<0:
                print("error\nel numero es menor a 0:")
                opcion=int(input("Desea continuar? 1)-si  0)-no: "))
            if opcion>1:
                print("error\nel numero es mayor a 1:")
                opcion=int(input("Desea continuar? 1)-si  0)-no: "))
            if opcion==0:
                comp=1
        except:
            print("Error ingrese los datos nuevamente")
    limpiar()
archivo(codemp,nom,edad,sexo,ecivil)#invoco a la funcion para cargar en el archivo
print("                                 FIN DE LA CARGA")
print("Desea ver la lista cargada?\n1)-si\n2)-no")
comp=0
while comp==0:
    try:
        opinforme=int(input("opcion:"))
        if opinforme==1:
            import lectura
            print("                          FIN DEL PROGRAMA")
            comp=1
        if opinforme==2:
            limpiar()
            print("                          FIN DEL PROGRAMA")
            comp=1
    except:
        print("error\ningrese nuevamente")