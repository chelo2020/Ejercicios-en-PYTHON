#Leer el siguiente archivo, cargar en una matriz, 
#ordenar alfabéticamente la descripción del 
#banco, por el métodoque le resulte más facil 

#Maestro de Bancos
#Cód. Bco.
#Desc. Banco

import os
def limpiar():
    os.system("cls")

def bienvenida(titulo,caracter="%"):
    print(titulo)
    print(caracter*len(titulo))

def consulta():
    comp=0
    while comp==0:
        try:
            op=int(input("1-crear un archivo nuevo: \n2-continuar agregando: 0-finaliza la carga\nopcion: "))
            if op==1:
                archivo=open("Banco.txt","w")
                archivo.close()
                break
            if op==2:
                archivo=open("Banco.txt","r")
                archivo.close()
                carga()
                break
            if op==0:
                print("Finaliza  el programa")
                limpiar()
                bienvenida("  FIN DEL PROGRAMA   ")
        except:
            print("la opcion no es la correcta: ")
            op=int(input("1-crear un archivo nuevo: \n2-continuar agregando:\n0=CIERRA EL PROGRAMA:\nopcion: "))

            
    

def abri_archivo(cont,cod_banco,desc_bco):
    archivo=open("Banco.txt","a")
    for x  in range(cont):
        archivo.write(str(cod_banco[x]))
        archivo.write(",")
        archivo.write(str(desc_bco[x]))
        archivo.write("\n")
    archivo.close()
    
    
def carga():
    limpiar()
    cod_banco=[]
    desc_bco=[]
    op=1
    cont=0
    while op!=2:
        bienvenida("    BIENVENIDOS AL PROGRAMA DE CARGA    ")
        co=int(input("Ingrese el codigo del Banco: "))
        cod_banco.append(co)
        comparacion=existe(co)
        if comparacion==False:
            desc=input("Ingrese el nombre del banco: ")
            desc_bco.append(desc)
            cont=cont+1
            op=int(input("1=seguir con la carga,2=finalizacion de la carga\nOpción: "))
            limpiar()
            if op<1 or op>2:
                print("La opcion no es la correcta\nVuelva a intentarlo")
                op=int(input("1=seguir con la carga,2=finalizacion de la carga\nOpción: "))
        else:
            print("El codigo ya existe")
    limpiar()
    abri_archivo(cont,cod_banco,desc_bco)
    consulta()

def existe(cod):
    archivo=open("Banco.txt","r")
    lista=archivo.readline()
    linea=lista.split(",")
    valor=False
    cont=0
    while lista!="":
        linea=lista.split(",")
        codigo=int(linea[0])
        if codigo==cod:
            cont=cont+1
        if cont>0:
            valor=True
        lista=archivo.readline()
    archivo.close()
    return valor


#Bloque principal
carga()