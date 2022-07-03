#Programa de ingreso (Altas) de datos, por medio de una pantalla de Carga.

#Cód. Empl.
#Nombre y Apellido
#S. Básico
#Categoría

#Valores en campos:
#Categoría: 1 = Mecánico, 2 = Conductor.
#////////////////////////////////////////////
#Se desea obtener informe según diseño:
#Padrón de Empleados:
#Cód. Empl.
#Nombre y Apellido
#S. Básico
#Observaciones
#Total
#Promedio sueldo:
#Promedio sueldo mecánico
#NOTA: La columna “Observaciones” deberá contener ‘Mecánico’ si el valor de “Categoría” 
# es igual a 1 y, contendrá ‘Conductor’ si el valor de “Categoría” es 2
#////////////////////////////////////////////////////////////////////////////////////////////

#funciones:
import os
def limpiar():#despeja la pantalla para que la presetacion sea mas prolija
    os.system("cls")


def carga(v1,v2,v3,v4):
   archivo=open("archivo1.txt","r")#abro el archivo en modo lectura para contar las lineas en caso de continuar escribiendo
   con=0
   lista=archivo.readline()
   while lista!="":
       con=con+1
       lista=archivo.readline()
   archivo.close()
   archivo=open("archivo1.txt","a")
   for x in range(cont):
       con=con+1
       archivo.write(str(con))
       archivo.write(",")
       archivo.write(v2[x])
       archivo.write(",")
       archivo.write(str(v3[x]))
       archivo.write(",")
       archivo.write(str(v4[x]))
       archivo.write("\n")
   archivo.close()


def lectura():#funcion para seleccionar la lectura o la escritura del archivo
   comp=0
   while comp!=1:#while infinito
       try:
           op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
           if op==1:
               archivo=open("archivo1.txt","w")
               archivo.close()
               break
           if op==2:
               archivo=open("archivo1.txt","r")
               archivo.close()
               break
           else:
               print("el parametro no es correcto")
               op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
       except:
            print("el parametro no es correcto")
   limpiar()
           


def bienvenida():
    print("                                 BIENVENIDOS ATLAS, SISTEMA DE CARGA:")
    print("")
    print("")

#Programa:

limpiar()
bienvenida()
lectura()


codem=[]
noemp=[]
sueldo=[]
cat=[]
cont=0
op=1

while op!=2:
   bienvenida()
   cont=cont+1
   codem.append(cont)
   lista1=input("Ingrese el nombre del empleado: ")
   noemp.append(lista1)
   booleano=False
   while booleano!=True:
       try:
           lista2=float(input("ingrese el sueldo del empleado: "))
           comprobacion=type(lista2)
           if comprobacion==float:
               booleano=True
       except:
           print("ERROR, A INGRESADO UN PARAMETRO INCORRECTO\nINGRESE NUEVAMENTE")
   sueldo.append(lista2)
   lista3=0
   while lista3>2 or lista3<1:
       try:
           lista3=int(input("Ingrese la categoria\n1)mecanico \n2)conductor\nopcion: "))
           if lista3>2 or lista3<1:
                print("error parametro incorrecto")
       except:
           print("ERROR, PARAMETRO INCORRECTO\nINGRESE NUEVAMENTE\n")
   cat.append(lista3)
   try:
       op=int(input("Desea continuar? si=1  no=2: "))
       if op==2:
            limpiar()
            print("fin de la carga")
       if op==1:
           limpiar()
   except:
       print("error el parametro no es correcto")
carga(codem,noemp,sueldo,cat)
limpiar()
bienvenida()
print("Desea ver la lista cargada?\n1)-si\n2)-no")
opinforme=2
while opinforme==2:
   try:
       opinforme=int(input("opcion:"))
       if opinforme==1:
           import lectura1
           print("                          FIN DEL PROGRAMA")
       if opinforme==2:
           limpiar()
           print("                          FIN DEL PROGRAMA")
   except:
       print("error\ningrese nuevamente")
    