#Realizar un programa de carga, según  diseño Fig 7, los archivos maestro
#  (clientes, artículos) ya poseen datos grabados en el disco rígido. 
#Proceso: 

#1) Ingresar la clave cliente, si es cero sale del programa, si no verificar si existe, en caso que no exista, mensaje: "no puede comprar porque no existe". caso contrario, se accede al archivo maestro de cliente y se imprime en pantalla el nombre y apellido.

#2) Se ingresa el numero de factura y la fecha. 

#3) Se ingresa el código de artículo, se verifica en archivo, en caso de que no exista, mensaje "no existe artículo, reingrese". Caso contrario se imprime en pantalla el detalle del artículo. 

#4) Se ingresa  el importe a pagar


#4) Se solicita 1 Grabar 2- cancelar (en el caso de grabar se genera el archivo de novedad según diseño Fig 3) .


#Figura 7 
#Pantalla de carga
#Cód. Cliente:xxx
#Nya: ZZZZZZZ
#Nro. De Factura: xxxxxx	Fecha: xx/xx/xx
#Cód. Artículo	Descripción Artículo 	Importe
#xxxx	zzzzzz	xxxxx
#1 - Graba	2- Cancela





#***************************************************************
#FUNCIONES GENERALES, IMPORTACION DE OTRO ARCHIVO .PY


from consultas import consultanomcliente as consulta_cliente

from consultas import consultanomarticulo as consulta_nomarticulo

from consultas import devcodpornombrecliente

from consultas import detalle_producto as detallep

from consultas import devcodpornombre

from consultas import consultaexistecliente

from consultas import en_stock

from consultas import suma_de_productos

from consultas import precio_por_unidad

from consultas import totalprecios

from consultas import facturas_por_fecha

from consultas import consuta_mov_cliente

from consultas import consulta_fact_art


import os
def limpiar():
    os.system("cls")


def encabezado():
    limpiar()
    print("                    BIENVENIDO AL SISTEMA DE CARGA:\n\nopciones:\n")

def retorno_de_carga():#variable para detener el sistema o no
    print("Desea finalizar? S= si  N=no")
    valor=input("opcion: ")
    return valor
#*************************************************************

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#MENU PRINCIPAL
def menu_principal():
    encabezado()
    op="s"
    while op=="s":
        encabezado()
        print("1)-carga de clientes")
        print("2)-carga de articulos")
        print("3)-venta")
        print("4)-consultas")
        print("5)-salir")
        opcion=int(input("opcion: "))
        if opcion==1:
            menu_carga_clientes()
        if opcion==2:
            menu_carga_articulos()
        if opcion==3:
            venta()
        if opcion==4:
            encabezado()
            submenu_ventas()
        if opcion==5:
            limpiar()
            print("******fin del programa********")
    print("fin del programa")
#----------------------------------------------------
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Función de submenu ventas
def submenu_ventas():
    print("1)-Informe por fecha")
    print("2)-Informe por cliente")
    print("3)-Informe por articulo")
    print("4)-Volver al menu")
    opcion_venta=int(input("opcion: "))
    if opcion_venta==1:
        fecha=input("Ingrese la fecha: aaaa-mm-dd\nopcion: ")
        facturas_por_fecha(fecha)
        print("desea volver al menu? s=si   n=no")
        opcion_menu=input("opcion: ")
        if opcion_menu=="s":
            menu_principal()
    if opcion_venta==2:
        valor=input("ingrese el nombre o el codigo del cliente: ")
        consuta_mov_cliente(str(valor))
        print("desea volver al menu? s=si   n=no")
        opcion_menu=input("opcion: ")
        if opcion_menu=="s":
            menu_principal()
    if opcion_venta==3:
        val_cod=int(input("ingrese el codigo del producto: "))
        consulta_fact_art(val_cod)
        print("desea volver al menu? s=si   n=no")
        opcion_menu=input("opcion: ")
        if opcion_menu=="s":
            menu_principal()
    if opcion_venta==4:
        menu_principal()
        
#////////////////////////////////////////////////////////
#       BLOQUE NUEVO:

#bloque de FUNCIONES PARA  proceso de carga y escritura de los clientes:

#MENU DE CARGA DE CLIENTES
def menu_carga_clientes():
    comp=0
    try:
        while comp!=1:#while infinito
            encabezado()
            op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\n3)-volver\nOpcion: "))
            if op==1:#con esta opcion creo un archivo desde 0
                archivo=open("clientes.txt","w")
                archivo.close()
                carga_clientes()
                break
            if op==2:#con esta opcion simplemente abro de manera provisoria en modo lectura para volver a cerrarlo y ejecutar la funcion de carga
                archivo=open("clientes.txt","r")
                archivo.close()
                carga_clientes()
            if op==3:
                menu_principal()
            else:
                print("el parametro no es correcto")
                op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
    except:
        print("PRESTA ATENCION!!")
#-------------------------------------------------------

#FUNCION DE ESCRITURA DEL ARCHIVO CLIENTE
def archivo_clientes(nombre,localidad,direccion,cont):#voy a cargar los datos del cliente en el archivo correspondiente
    archivo=open("clientes.txt","r")
    cargados=len(archivo.readlines())#con este proceso obtengo la cantidad de registros correlativos en el archivo, para asi poder continuar la carga
    archivo.close()
    con=cargados+1
    archivo=open("clientes.txt","a")
    for x in range(cont):
        archivo.write(str(con))
        archivo.write(",")
        archivo.write(str(nombre[x]))
        archivo.write(",")
        archivo.write(str(localidad[x]))
        archivo.write(",")
        archivo.write(str(direccion[x]))
        archivo.write("\n")
    archivo.close()
#---------------------------------------------------------------

#FUNCION DE CARGA DE CLIENTES:
def carga_clientes():
    encabezado()
    cont=0
    lista_nombres=[]
    lista_localidad=[]
    lista_direccion=[]
    cont_carga="s"
    while cont_carga=="s":
        encabezado()
        nombre=input("ingrese el nombre del cliente: ")
        vconsulta=consultaexistecliente(nombre)
        if vconsulta==False:
            lista_nombres.append(nombre)
            localidad=input("ingrese la localidad: ")
            lista_localidad.append(localidad)
            direccion=input("ingrese la direccion: ")
            lista_direccion.append(direccion)
            cont=cont+1
            cont_carga=input("desea continuar la carga?: s=si  n=no\nopcion: ")
            if cont>0:
                op_carga=input("desea guardar lo cargado? s=si  n=no\nopcion: ")
                if op_carga=="s":
                    archivo_clientes(lista_nombres,lista_localidad,lista_direccion,cont)
                else:
                    menu_principal()
        else:
            print("el cliente ya existe")
            el=int(input("volver al menu=1    ingresar nuevocliente=2\nopcion: "))
            if el==1:
                cont_carga="n"
                menu_principal()
            if el==2:
                encabezado()
    menu_principal()
#----------------------------------------------------------
#           FIN DEL BLOQUE


#//////////////////////////////////////////////////////////
#           BLOQUE NUEVO:

#BLOQUE DE FUNCIONES PARA PROCESO DE CARGA DE LOS ARTICULOS:

#MENU DE CARGA DE ARTICULOS:
def menu_carga_articulos():
    comp=0
    try:
        while comp!=1:#while infinito
            encabezado()
            op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\n3)-volver\nOpcion: "))
            if op==1:#con esta opcion creo un archivo desde 0
                archivo=open("articulos.txt","w")
                archivo.close()
                carga_articulos()
                break
            if op==2:#con esta opcion simplemente abro de manera provisoria en modo lectura para volver a cerrarlo y ejecutar la funcion de carga
                archivo=open("articulos.txt","r")
                archivo.close()
                carga_articulos()
            if op==3:
                menu_principal()
            else:
                print("el parametro no es correcto")
                op=int(input("1)-Crear un archivo nuevo: \n2)-Agregar contenido al existente:\nOpcion: "))
    except:
        print("PRESTA ATENCION!!")

#----------------------------------------------------------------

#FUNCION CARGA DE ARTICULOS:
def carga_articulos():
    encabezado()
    cont_carga_art="s"
    cont=0
    lista_nombreart=[]
    lista_precio=[]
    lista_stock=[]
    while cont_carga_art=="s":
        nombre_art=input("ingrese el nombre del articulo: ")
        valor_consulta=consulta_nomarticulo(nombre_art)
        if valor_consulta==False:
            lista_nombreart.append(nombre_art)
            precio=input("ingrese el precio del articulo: ")
            lista_precio.append(precio)
            stock=input("ingrese la cantidad en stock: ")
            lista_stock.append(stock)
            cont=cont+1
            cont_carga_art=input("desea continuar con la carga?: s=si  n=no\nopcion:")
            if cont>0:
                op_carga=input("desea guardar lo cargado? s=si  n=no\nopcion: ")
                if op_carga=="s":
                    archivo_articulos(lista_nombreart,lista_precio,lista_stock,cont)
                else:
                    menu_principal()
        else:
            print("el articulo ya existe")
            el=int(input("volver al menu=1    ingresar otro producto=2\nopcion: "))
            if el==1:
                cont_carga_art="n"
                menu_principal()
            if el==2:
                encabezado()
    menu_principal()
#--------------------------------------------------------------        

#FUNCION PARA LA ESCRITURA DEL ARCHIVO ARTICULOS:
def archivo_articulos(nombre_art,precio,cantidad_stock,cont):#voy a cargar los datos del articulo en el archivo correspondiente
    archivo=open("articulos.txt","r")
    cargados=len(archivo.readlines())#con este proceso obtengo la cantidad de registros correlativos en el archivo, para asi poder continuar la carga
    archivo.close()
    con=cargados+1
    archivo=open("articulos.txt","a")
    for x in range(cont):
        archivo.write(str(con))
        archivo.write(",")
        archivo.write(str(nombre_art[x]))
        archivo.write(",")
        archivo.write(str(precio[x]))
        archivo.write(",")
        archivo.write(cantidad_stock[x])
        archivo.write("\n")
    archivo.close()
#--------------------------------------------------------------
#              FIN DEL BLOQUE
#//////////////////////////////////////////////////////////////////
#          BLOQUE NUEVO:

#FUNCION DE CARGA DE VENTA

def venta():
    cont_carga_vent="s"
    while cont_carga_vent=="s":
        encabezado()
        nomb_cliente=input("ingrese el nonmbre del cliente: ")
        compcliente=consulta_cliente(nomb_cliente)
        if compcliente==True:
            cod_cliente=devcodpornombrecliente(nomb_cliente)#codigo del cliente
            print("cargar por nombre: 1  o por cod de articulo:2 ")
            opcionv=int(input("opcion: "))
            if opcionv==1:
                subtotal=[]
                lista_productos=[]
                continuar="s"
                item=0
                contador=0
                while continuar=="s":
                    nom_articulo=input("ingrese el nombre del articulo: ")
                    resultado=consulta_nomarticulo(nom_articulo)
                    if resultado==True:
                        contador=contador+1
                        codigo=devcodpornombre(nom_articulo)#codigo del producto
                        preciounitario=precio_por_unidad(nom_articulo)
                        cantidad=int(input("ingrese la cantidad: "))
                        subsuma=suma_de_productos(nom_articulo,cantidad)
                        subtotal.append(subsuma)
                        item=item+1
                        lista_productos.append([item,codigo,nom_articulo,preciounitario,cantidad,subsuma])                
                        continuar=input("desea continuar la carga? s=si  n=no\nopcion: ")
                        if contador>2:
                            print("maximo de carga alcanzada")
                            cont_carga_vent=input("desea realizar otra factura? s=si  n=no\nopcion: ")
                            menu_principal()
                    totales=totalprecios(subtotal)
                    print("el total es: ",totales)
                cont_carga_vent=input("desea realizar otra factura? s=si  n=no\nopcion: ")
            archivo_facturas(cod_cliente,nomb_cliente,lista_productos,totales)
        else:
            el=int(input("volver al menu=1    ingresar otro nombre=2\nopcion: "))
            if el==1:
                menu_principal()
            if el==2:
                encabezado()
    menu_principal()
#---------------------------------------------------------------
#FUNCION PARA LA ESCRITURA DEL ARCHIVO FACTURA
def archivo_facturas(cod_cliente,nombre_cliente,listaproductos,importetotal):
    from datetime import date
    fecha=date.today()
    archivo=open("facturas.txt","r+")
    cargados=len(archivo.readlines())#con este proceso obtengo la cantidad de registros correlativos en el archivo, para asi poder continuar la carga
    archivo.close()
    con=cargados+1
    archivo=open("facturas.txt","a")
    archivo.write(str(con))
    archivo.write(",")
    archivo.write(str(fecha))
    archivo.write(",")
    archivo.write(str(cod_cliente))
    archivo.write(",")
    archivo.write(str(nombre_cliente))
    archivo.write(",")
    archivo.write(str(listaproductos))
    archivo.write(",")
    archivo.write(str(importetotal))
    archivo.write("\n")
    archivo.close()


#             FIN DEL BLOQUE
#//////////////////////////////////////////////////////////////////
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~4
#             BLOQUE NUEVO

#................................................................
#programa

menu_principal()