#//////////////////BLOQUE DE CONSULTAS//////////////////
def consultaexistecliente(nombre):
    archivo=open("clientes.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    verdad=0
    while lista!="":
        lineas=lista.split(",")
        nomb=str(lineas[1])
        if nomb==nombre:
            verdad=1
        lista=archivo.readline()
    archivo.close()
    if verdad==1:
        return True
    else:
        return False

#---------------------------------------------------
#consulta de nombre de clientes para opcion listado
def consultanomcliente(nombre):
    archivo=open("clientes.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    verdad=0
    while lista!="":
        lineas=lista.split(",")
        nomb=str(lineas[1])
        if nomb==nombre:
            verdad=1
        lista=archivo.readline()
    archivo.close()
    if verdad==1:
        return True
    else:
        print("el cliente no existe")
        return False
#-------------------------------------------------------

#consutla de codigo de articulo
def consultacodarticulo(codigo):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    cont=0
    total_lineas=len(archivo.readlines())
    verdad=0
    while lista!="":
        lineas=lista.split(",")
        numart=int(lineas[0])
        if numart==codigo:
            verdad=1
            return True
        if numart!=codigo:
            cont=cont+1
        if cont==total_lineas and verdad==0:
            print("el codigo no existe, ingrese al menu de carga para listar un nuevo cliente")
            return False
        lista=archivo.readline()
    archivo.close()
#-----------------------------------------------

#consulta nombre de articulos:

def consultanomarticulo(nombre):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    verdad=0
    while lista!="":
        lineas=lista.split(",")
        nomb=str(lineas[1])
        if nomb==nombre:
            verdad=1
        lista=archivo.readline()
    archivo.close()
    if verdad==1:
        return True
    else:
        print("el articulo no existe")
        return False

#------------------------------------------------
#fin del bloque de consultas

#////////////////////////////////////////////////////////
#bloque de retonrno de datos

#CAMBIA NOMBRE POR NUMERO DE CODIGO DEL ARTICULO
def devcodpornombre(nomart):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        nombreref=str(lineas[1])
        if nombreref==nomart:
            codigo=int(lineas[0])
        lista=archivo.readline()
    archivo.close()
    return codigo
#----------------------------------------------------
#CAMBIA EL NOMBRE DEL CLIENTE POR EL CODIGO DEL CLIENTE:
def devcodpornombrecliente(nombre):
    archivo=open("clientes.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        nombreref=str(lineas[1])
        if nombreref==nombre:
            codigo=int(lineas[0])
        
        lista=archivo.readline()
    archivo.close()
    return codigo
    

#DEVUELVE LOS DETALLER DEL PRODUCTO:
def detalle_producto(codigo):
    detalle=[]
    archivo=open("articulos.txt","r")
    archivo.seek(codigo-1)
    lista=archivo.readline()
    lineas=lista.split(",")
    numcod=int(lineas[0])
    nombre=lineas[1]
    precio=float(lineas[2])
    stock=int(lineas[3])
    detalle[numcod]=nombre,precio,stock
    archivo.close()
    return detalle
#-------------------------------------------------------------
#CONSULTA STOCK:
def en_stock(nombre):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        nombreref=str(lineas[1])
        if nombreref==nombre:
            cantidad=int(lineas[3])
        lista=archivo.readline()
    archivo.close()
    return cantidad
#------------------------------------------------------------
#PRECIO POR UNIDAD:
def precio_por_unidad(nombre):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        nombreref=str(lineas[1])
        if nombreref==nombre:
            valor=int(lineas[2])
        lista=archivo.readline()
    archivo.close()
    return valor
    
#-------------------------------------------------------------
#SUMA DE VALORES DE LOS PRODUCTOS
def suma_de_productos(nombre,cantidad):
    archivo=open("articulos.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        nombreref=str(lineas[1])
        if nombreref==nombre:
            valor=int(lineas[2])*cantidad
        lista=archivo.readline()
    archivo.close()
    return valor
#-----------------------------------------------
#suma los valores de la suma de los subtotales de la lista de los productos
def totalprecios(lista):
    suma=0
    for x in  lista:
        suma=suma+x
    return suma
#---------------------------------------------------
#Consulta por fecha:
def facturas_por_fecha(fecha):
    print("************************************")
    archivo=open("facturas.txt","r")
    lista=archivo.readline()
    linea=lista.split(",")
    while lista!="":
        linea=lista.split(",")
        f=str(linea[1])
        if f==fecha:
            cont_cliente=linea
            precio_final=len(cont_cliente)
            print("fecha: ",linea[1],"    *nombre cliente: ",linea[3],"\ncodigo cliente: ",linea[2],"\n numero factura: ",linea[0],"\n")
            print("codigo producto: ",linea[5])
            if precio_final>11:
                print("codigo seg producto: ",linea[11])
            if precio_final>17:
                print("tercer producto: ", linea[17])
            print("\ntotal: ",cont_cliente[precio_final-1])
            print("----------------------------------------------")
        lista=archivo.readline()
    archivo.close()
#--------------------------------------------------------------------
#consulta por clientes: 
def consuta_mov_cliente(cliente):
    archivo=open("facturas.txt","r")
    lista=archivo.readline()
    linea=lista.split(",")
    cont=0
    while lista!="":
        linea=lista.split(",")
        nom=str(linea[3])
        cod=str(linea[2])        
        if cliente==nom:
            cont=cont+1
            codcl=int(linea[2])
            nombre=str(linea[3])
            fecha=str(linea[1])
            numfactura=int(linea[0])
            total=linea[len(linea)-1]
            if cont==1:
                print("\ncodigo cliente: ",codcl,"         nombre: ",nombre,"\n")
                print("*Fecha:         *Fact Nº:     *Importe    ")
            print(fecha, "     ",numfactura,"           ",total)
            print("-----------------------------------------------")
        if cliente==cod:
            cont=cont+1
            codcl=int(linea[2])
            nombre=str(linea[3])
            fecha=str(linea[1])
            numfactura=int(linea[0])
            total=linea[len(linea)-1]
            if cont==1:
                print("\ncodigo cliente: ",codcl,"         nombre: ",nombre,"\n")
                print("*Fecha:         *Fact Nº:     *Importe    ")
            print(fecha, "     ",numfactura,"           ",total)
            print("-----------------------------------------------")
        lista=archivo.readline()
    archivo.close()
#-------------------------------------------------------------------

#consulta por articulos facturados:

def consulta_fact_art(valor):
    print("/////////////////////////////////////////////")
    archivo=open("facturas.txt","r")
    lista=archivo.readline()
    linea=lista.split(",")
    cont=0
    cont2=0
    while lista!="":
        linea=lista.split(",")
        longitud=len(linea)
        codproduct1=int(linea[5])
        if longitud>11:
            codproduct2=int(linea[11])
        if longitud>17:
            codproduct3=int(linea[17])
        if codproduct1==valor:
            if codproduct1==valor:
                cont=cont+1
                print("codigo art: ", linea[5])
                print("codigo cliente          nombre                num factura     fecha     importe")
                print("  ",linea[2],"                   ",linea[3],"               ",linea[0],"          ",linea[1],"   ",linea[9])
            if longitud>11:
                if codproduct2==valor:
                    cont=cont+1
                    if cont>1:
                        print("  ",linea[2],"                   ",linea[3],"             ",linea[0],"          ",linea[1],"   ",linea[15])
            if longitud>17:
                if codproduct3==valor:
                    cont+1
                    if cont>1:
                        print("  ",linea[2],"                   ",linea[3],"             ",linea[0],"          ",linea[1],"   ",linea[21])
        if longitud>11:
            if codproduct2==valor:
                cont2=cont2+1
                print("codigo art: ", linea[11])
                print("codigo cliente          nombre                num factura     fecha     importe")
                print("  ",linea[2],"                   ",linea[3],"               ",linea[0],"          ",linea[1],"   ",linea[15])
            if longitud>17:
                if codproduct3==valor:
                    cont2=cont2+1
                    if cont2>1:
                        print("  ",linea[2],"                   ",linea[3],"             ",linea[0],"          ",linea[1],"   ",linea[21])    
        if longitud>17:
            if codproduct3==valor:
                print("codigo art: ", linea[17])
                print("codigo cliente          nombre                num factura     fecha     importe")
                print("  ",linea[2],"                   ",linea[3],"               ",linea[0],"          ",linea[1],"   ",linea[21])
        print("-----------------------------------------------")
        lista=archivo.readline()
    archivo.close()