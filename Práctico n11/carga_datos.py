#Fig 2
#Pantalla de carga de factura de compra
#Cód. Cte.
#Nombre Apellido:
#Fecha
#N° Factura.
#Importe
#G=Grabar
#C=Cancelar

import os
def limpiar():
    os.system("cls")

def bienvenida(titulo,caracter="#"):
    print(titulo)
    print(caracter*len(titulo))

def consulta():
    opcion=0
    while opcion==0:
        opcion=int(input("Digite:\n1=Nuevo archivo\n2=Continuar cargaando\nOpcion: "))
        if opcion==1:
            archivo=open("carga_datos.txt","w")
            archivo.close
            break
        if opcion==2:
            archivo=open("carga_datos.txt","r")
            archivo.close
            break
        if opcion!=1 or opcion!=2:
            print("Codigo incorrecto, vuelva a intentarlo")
            opcion=int(input("Digite:\n1=Nuevo archivo\n2=Continuar cargaando\nOpcion: "))
    limpiar()

def carga(v1,v2,v3,v4,v5):
    archivo=open("carga_datos.txt","r")
    contador=0
    lista=archivo.readline()
    while lista!="":
        contador=contador+1
        lista=archivo.readline()
    archivo.close()
    archivo=open("carga_datos.txt","a")
    for x in range(cont):
        contador=contador+1
        archivo.write(str(contador))
        archivo.write(",")
        archivo.write(str(v2[x]))
        archivo.write(",")
        archivo.write(str(v3[x]))
        archivo.write(",")
        archivo.write(str(v4[x]))
        archivo.write(",")
        archivo.write(str(v5[x]))
        archivo.write("\n")
    archivo.close

def informe():
    archivo=open("carga_datos.txt","r")
    print(archivo.read())
    archivo.close()



#Bloque Principal de Carga de Datos


cod_cte=[]
nom_ape=[]
fecha=[]
n_factura=[]
importe=[]
cont=0
continuar="s"
while continuar=="s":
    bienvenida("   Bienvenido al programa de Carga   ")
    consulta()
    cont=cont+1
    cod_cte.append(cont)
    nom=input("Ingrese el nombre y apellido del cliente: ")
    nom_ape.append(nom)
    fec=input("Ingrese la fecha de la compra, formato dd/mm/aa: ")
    fecha.append(fec)
    n_f=int(input("Ingrese el numero de factura del cliente: "))
    n_factura.append(n_f)
    impo=int(input("Ingrese el monto de la compra realizada: "))
    importe.append(impo)
    continuar=input("Digite\ns=si desea continuar\nn=si no desea continuar\nOpcion: ")
    limpiar()
    if continuar!="s":
        bienvenida("     FIN DEL PROGRAMA    ")


#Bloque principal

carga(cod_cte,nom_ape,fecha,n_factura,importe)

