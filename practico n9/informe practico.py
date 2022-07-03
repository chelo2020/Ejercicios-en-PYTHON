#informe, donde la lectura del archivo nos retorno una matriz
#n-filas y con dos columnas

def lectura_arch():
    archivo=open("Banco.txt","r")
    lista=archivo.readline()
    lineas=lista.split(",")
    cod_banco=[]
    desc_bco=[]
    while lista!="":
        lineas=lista.split(",")
        cod=str(lineas[0])
        cod_banco.append(cod)
        des=str(lineas[1])
        desc_bco.append(des)
        lista=archivo.readline()
    archivo.close()
    return cod_banco, desc_bco,

def ordenar():
    desc_bco=lectura_arch()
    longitud=int(len(desc_bco[0]))
    for x in range(longitud-1):
        for k in range((longitud-1)-x):
            if desc_bco[1][k]>desc_bco[1][k+1]:
                auxcod=desc_bco[0][k]
                auxdesc=desc_bco[1][k]
                desc_bco[0][k]=desc_bco[0][k+1]
                desc_bco[1][k]=desc_bco[1][k+1]
                desc_bco[0][k+1]=auxcod
                desc_bco[1][k+1]=auxdesc
    print("codigo "        "Descripcion")
    for x in range(len(desc_bco[0])):
        print("\n",desc_bco[0][x],"     ", desc_bco[1][x])
        

def cantidad_bancos():
    cod_banco=lectura_arch()
    longitud=int(len(cod_banco[0]))
    contador=0
    for x in range(longitud):
        contador=contador+1
        
    print("La cantidad de bancos ingresados es de : ",contador)

#Bloque principal:

ordenar()
cantidad_bancos()
