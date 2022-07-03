#Fig 1
#Maestro de Clientes

#Cód. Cliente            Nombre y Apellido
#   1                         Pepe Jose
#   2                         María josefina

#El código de Articulo se considera como clave principal o primaria (PK)
#----------------------------------------------------------------
#Fig 2
#Maetro Artículo 

#Cód. Articulo            Desc. Artículo
#  10                      Coca Cola
#  11                     Leche Sancor
#-----------------------------------------------------------------
#Fig 3
#Novedades

#Cód. Cli.  Cod. Articulo  Nro. Factura       Fecha        Importe
#   2            10            101           01/05/2020      150
#   2            11            101           01/05/2020      200
#   1            11            102           02/05/2020      500

#El codigo No. de Factuta se considera como clave secundaria (FK)
#-------------------------------------------------------------------

#**Realizar el ejercicio:  Generar el siguiente informe, ordenado alfabeticamente por cliente.  

#Informe por ordenado alfabéticamente por Cliente
 
#Cód. Artículo: 11                       Desc. Artículo:  Leche Sancor
#Cód. Cli.     Nombre y Apellido   Nro. De Factura       Fecha        Importe
#   2            María josefina    
# 
#   101               01/05/2020       200
#   1            Pepe Jose           102               02/05/2020       500

#TOTAL: 700


#---------------------------------------------------------------------
def nomporcod(cod_cliente):
    archivo=open("clip9.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        codreref=int(lineas[0])
        if codreref==cod_cliente:
            nombre=str(lineas[1])
        lista=archivo.readline()
    archivo.close()
    return nombre

def nombre_art(cod_arti):
    archivo=open("art9.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    while lista!="":
        lineas=lista.split(",")
        ref=int((lineas[0]))
        if ref==cod_arti:
            nombre1=str(lineas[1])
        lista.archivo.readline()
    archivo.close()
    return nombre1

def diccionario_novedades():
    arch=open("novp9.txt","r")
    l_cod_cli=[]
    l_cod_art=[]
    l_num_fact=[]
    l_fecha=[]
    l_importe=[]
    lista=arch.readline()
    linea=lista.split(",")
    while lista!="":
        linea=lista.split(",")
        cod_cli=int(linea[0])
        l_cod_cli.append(cod_cli)
        cod_art=int(linea[1])
        l_cod_art.append(cod_art)
        num_fact=int(linea[2])
        l_num_fact.append(num_fact)
        fecha=linea[3]
        l_fecha.append(fecha)
        importe=int(linea[4])
        l_importe.append(importe)
        lista=arch.readline()
    arch.close()
    cont=len(l_cod_art)-1
    for x in range(cont-1):#ordeno por articulo
        for k in range(cont-x):
            if l_cod_art[k]>l_cod_art[k+1]:
                aux1=l_cod_cli[k]
                aux2=l_cod_art[k]
                aux3=l_num_fact[k]
                aux4=l_fecha[k]
                aux5=l_importe[k]
                l_cod_cli[k]=l_cod_cli[k+1]
                l_cod_art[k]=l_cod_art[k+1]
                l_num_fact[k]=l_num_fact[k+1]
                l_fecha[k]=l_fecha[k+1]
                l_importe[k]=l_importe[k+1]
                l_cod_cli[k+1]=aux1
                l_cod_art[k+1]=aux2
                l_num_fact[k+1]=aux3
                l_fecha[k+1]=aux4
                l_importe[k+1]=aux5

    dicc_por_art={}#creo un diccionario para cargar el indice codigo de articulo
    lista=[]#creo un lista para guardar en el diccionario
    nom_cliente=nomporcod(l_cod_cli[0])#cambio el cod cliente por el nombre
    lista.append([l_cod_cli[0],nom_cliente,l_num_fact[0],l_fecha[0],l_importe[0]])#agrego los datos a la lista
    comp=l_cod_art[0]#defino el primer valor de la variable a comparar en el bucle
    cont=1
    for x in range(1, len(l_cod_art)):
        if cont==len(l_cod_art)-1:#si contador llega a la ultima posicion de codigo articulo
                nom_cliente=nomporcod(l_cod_cli[x])#llama a la funcion para cambiar el codigo por el nombre 
                lista.append([l_cod_cli[x],nom_cliente,l_num_fact[x],l_fecha[x],l_importe[x]])#agrego los valores de esta posicion a la lista
                dicc_por_art[comp]=lista#finalmente cargo el diccionario con el ultimo valor de la lista
                
        else:
            if comp == l_cod_art[x]:#si la posicion anterior es igual a la actual

                nom_cliente=nomporcod(l_cod_cli[x])#llama a la funcion para cambiar el codigo por el nombre
                lista.append([l_cod_cli[x],nom_cliente,l_num_fact[x],l_fecha[x],l_importe[x]])#agrego los datos a la lista
                cont=cont+1
                   
            else:#si la posicion actual es diferente
                dicc_por_art[comp]=lista#cargo los valores de la lista al diccionario
                comp=l_cod_art[x]#defino la nueva posicion para comparar con la siguiene
                lista=[]#reseteo la lista para carga los valores del nuevo indice
                nom_cliente=nomporcod(l_cod_cli[x])#llama a la funcion para cambiar el codigo por el nombre
                lista.append([l_cod_cli[x],nom_cliente,l_num_fact[x],l_fecha[x],l_importe[x]])#agrego los datos de la posicion actual a la lista
                cont=cont+1
    return dicc_por_art
    
#----------------------------------------------------------------------------------------
#                             programa
diccionario = diccionario_novedades()


#ordeno el diccionario
for indice in diccionario:#me entro en el indice
    longitud=len(diccionario[indice])-1
    for x in range(longitud):
        for k in range(longitud-x):
            if diccionario[indice][k][1]>diccionario[indice][k+1][1]:
                aux1=diccionario[indice][k][0]
                aux2=diccionario[indice][k][1]
                aux3=diccionario[indice][k][2]
                aux4=diccionario[indice][k][3]
                aux5=diccionario[indice][k][4]
                diccionario[indice][k][0]=diccionario[indice][k+1][0]
                diccionario[indice][k][1]=diccionario[indice][k+1][1]
                diccionario[indice][k][2]=diccionario[indice][k+1][2]
                diccionario[indice][k][3]=diccionario[indice][k+1][3]
                diccionario[indice][k][4]=diccionario[indice][k+1][4]
                diccionario[indice][k+1][0]=aux1
                diccionario[indice][k+1][1]=aux2
                diccionario[indice][k+1][2]=aux3
                diccionario[indice][k+1][3]=aux4
                diccionario[indice][k+1][4]=aux5


#informe:

for indice in diccionario:
    cont=0    
    print("\n**codigo del Producto: ", indice,"      Nombre del producto:  ")
    print("codigo cliente      nombre cliente       num factura     fecha     monto   ")
    print("-----------------------------------------------------------------------------")
    for lista in diccionario[indice]:
        print("    ",lista[0],"        ",lista[1],"           ",lista[2],"       ",lista[3],"  ",lista[4])
        cont=cont+lista[4]
    print("TOTAL:  ",cont)
    print("*****************************************************************************\n\n")    


