#Carga de datos de personas (Alta de personas)

#1) Cargar los datos que exista en el archivo 
# persona.dat en un dicionario. 

#2) Se ingresa la clave (código de persona). 
# Si la clave es cero, se sale de programa. 
# Si la clave no es cero, se accede al Diccionario
#   y se verifica que la misma exista. 
# En caso de que exista la clave, 
# se emite un mensaje “No se puede dar de alta, 
# clave ya existe. Sólo puede modificar o borrar.”

#En el caso de que la clave no exista, 
# se procede a cargar y guardar la información 
# necesaria en el archivo persona.dat

#Ingresar el Apelldo y nombre: 
# (no puede superar 30 caracteres de longitud).

#El sexo (1=Varon, 2=Mujer) verificar  
# si el valor ingresado es correcto. 
# Si se ingresó un valor incorrecto, 
# imprimir en pantalla “Prestá atención”.

#Ingresar el sueldo (No puede ser cero)

#Se ingresa la sucursal : 1=Posadas  2=Garupa 
# 3- Candelaria. Nuevamente, 
# si se ingresa un valor incorrecto, 
# imprimir “Prestá Atención.”

#Cuando ingresa la sucursal, buscar en una tupla, 
# la sucursal,  e imprimir el nombre de la sucursal 
# (Ej. 2 - Garupá)

#Al terminar el ingreso de datos, se pregunta por 
# GRABAR (1) o Cancelar (2). Imprimir el mensaje 
# de error correspondiente si se ha 
# ingresado un valor incorrecto.

import os
def limpiar():
    os.system("cls")

from lectura import comprobacion as check#importo la funcion comprobar del programa de lectura

def titulo_subrayado(titulo,caracteres="-"):#funcion para carga del titulo
    limpiar()#agrego la funcion limpiar
    print(titulo)
    print(caracteres*len(titulo))

def main_menu():#menu principal donde se van a seleccionar las opciones
    opcion=0#variable que ejecutara la carga mientras sea 0
    limpiar()
    titulo_subrayado("           BIENVENIDOS AL PROGRAMA DE CARGA      \n\n")
    print("Opciones: ingrese el numero de la opcion deseada")
    print("1)-Carga de empleados")
    print("2)-Consulta por sucursal")
    print("3)-Consulta por dni\n")
    while opcion==0:
        try:
            opcion=int(input("ingrese la opcion:"))#variable para seleccionar las opciones
            if opcion==1:#carga la funcion de submenu
                sub_menu()#invoca a la funcion de submenu para cargar o crear el archivo, esta funcion es llamada desde la linea 92
            if opcion==2:#si se carga la opcion 2 invoca a la funcion del archivo lectura
                from lectura import por_sucursal as con_sucursal#funcion invocada desde el archivo lectura
                con_sucursal(int(input("ingrese el numero de la sucursal: ")))#solicito el ingreso de un valor como parametro para que se ejecute la funcion
                volver=int(input("\nPresione 1 para volver al menu, 2 para salir: "))#variable para retornar o no al menu principal
                if volver==1:
                    main_menu()
                if volver==2:
                    limpiar()
                    print("Fin del programa")
                    opcion=1
            if opcion==3:#si se carga la opcion 3 se invoca a la funcion listado por dni desde el programa de lectura
                from lectura import por_dni as con_dni
                con_dni(int(input("ingrese el numero de dni: ")))#solicita el ingreso de un parametro para que se ejecute la funcion
                volver=int(input("\nPresione 1 para volver al menu, 2 para salir: "))#variable para volver o no al menu
                if volver==1:
                    main_menu()
                if volver==2:
                    limpiar()
                    print("Fin del programa")
                    opcion=1           
        except:
            print("PRESTA ATENCION!")
            opcion=0
    
    
def sub_menu():#funcion para seleccionar la lectura o la escritura del archivo
    comp=0
    limpiar()
    titulo_subrayado("           BIENVENIDOS AL PROGRAMA DE CARGA      \n\n")
    try:
        while comp!=1:#while infinito
            op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
            if op==1:#con esta opcion creo un archivo desde 0
                archivo=open("empleados.txt","w")
                archivo.close()
                carga_empleados()
                break
            if op==2:#con esta opcion simplemente abro de manera provisoria en modo lectura para volver a cerrarlo y ejecutar la funcion de carga
                archivo=open("empleados.txt","r")
                archivo.close()
                carga_empleados()
            
            else:
                print("el parametro no es correcto")
                op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
    except:
        print("PRESTA ATENCION!!")
    limpiar()
    
        
def archivo(v1,v2,v3,v4,v5,cont):
    archivo=open("empleados.txt","r")#abro el archivo en modo lectura para contar las lineas en caso de continuar escribiendo
    con=0
    lista=archivo.readline()
    while lista!="":
        con=con+1
        lista=archivo.readline()
    archivo.close()
    archivo=open("empleados.txt","a")#abro el archivo en modo agregar
    for x in range(cont):#con este for comienzo a escribir desde la ultima linea por debajo de lo ultimo agregado
        con=con+1
        archivo.write(str(v1[x]))
        archivo.write(",")
        archivo.write(v2[x])
        archivo.write(",")
        archivo.write(str(v3[x]))
        archivo.write(",")
        archivo.write(str(v4[x]))
        archivo.write(",")
        archivo.write(str(v5[x]))
        archivo.write("\n")
    archivo.close()
           
def carga_empleados():
    opcion="s"
    cont=0    
    list_codemp=[]
    list_nom=[]
    list_sexo=[]
    list_sueldo=[]
    list_sucursal=[]
    while opcion=="s":
        cont=cont+1
        try:
            codemp=int(input("Ingrese el dni del empleado 0 para salir: "))
            valor=check(codemp)
            if valor==False:
                volver=input("presione enter para vovler al menu: ")
                main_menu()
            if codemp==0:
                print("Fin del programa")
                opcion="n"
            list_codemp.append(codemp)
        except:
            print("ERROR: El valor ingresado no es correcto")
        longitud=30#defino la longitud maxima de caracteres permitidos en el ingreso del nombre
        nombre=input("ingrese el nombre y el apellido: ")
        if len(nombre)>longitud:#chequea que la longitud este dentro del parametro, si es mayor se ejecuta
            print("ERROR\nEl se permiten solo 30 caracteres:")
            nombre=input("ingrese el nombre y el apellido: ")#vuelve a solicitar la carga del nombre
        list_nom.append(nombre)
        try:
            sexo=0
            while sexo!=1 and sexo!=2:#mientras el valor sexo sea diferente de 1 y 2
                sexo=int(input("ingrese el sexo\n1)-varon\n2)-mujer\nopcion: "))
            list_sexo.append(sexo)
        except:
            print("ERROR: el valor ingresado no es correcto")
        try:
            sueldo=0
            while sueldo==0:#la carga de sueldo se va a ejecutar siempre que el valor sea 0
                sueldo=float(input("ingrese el sueldo: "))
            list_sueldo.append(sueldo)
        except:
            print("ERROR: el dato ingresado no es correcto")
            sueldo=0
        sucursal=0
        try:
            while sucursal==0:
                sucursal=int(input("ingrese la sucursal:\n1)-Posadas, 2)-Garupa, 3)-Candelaria\nopcion: "))
                if sucursal<1 or sucursal>3:
                    print("ERROR: el valor ingresado no es correcto")
                    sucursal=0
            list_sucursal.append(sucursal)
        except:
            print("error, Presta atencion!!")
        opcion=input("desea continuar la carga?\ns=si  n=no\nopcion: ")
    limpiar()
    print("Los datos cargados hasta el momento son de: ")
    for x in range (len(list_codemp)):        
        print(list_codemp[x],list_nom[x])
    print("desea guardar los datos? s/n")
    guardado=input("opcion: ")
    if guardado=="s":
        archivo(list_codemp,list_nom,list_sexo,list_sueldo,list_sucursal,cont)
        print("guardado realizado")
        volver=input("volver al menu?: s/n")
        if volver=="s":
            main_menu()
        if volver!="s":
            print("fin del programa")
            opcion="n"






#----------------------------Bloque Principal----------------------------
titulo_subrayado("           BIENVENIDOS AL PROGRAMA DE CARGA      ")
main_menu()








