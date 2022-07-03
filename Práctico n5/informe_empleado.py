def titulo_subrayado(titulo, caracter="+"):
    print(titulo)
    print(caracter*len(titulo))


def archi_abrir():
    archivo=open("empleado.txt","r")
    cont=0
    codigo=[]
    nom=[]
    sueldo=[]
    categoria=[]
    cont=0
    lista=archivo.readline()
    lineas=lista.split(",")

    while lista!="":
        lineas=lista.split(",")
        cont=cont+1
        lista1=int(lineas[0])
        codigo.append(lista1)
        lista2=lineas[1]
        nom.append(lista2)
        lista3=float(lineas[2])
        sueldo.append(lista3)
        lista4=int(lineas[3])
        categoria.append(lista4)
        lista=archivo.readline()
    archivo.close()

    for x in range(cont):
        print(codigo[x],nom[x],sueldo[x],categoria[x])
        print("---------------------------------------")

    contsueldo=0
    for x in range(cont):
        if sueldo[x]>0:
            contsueldo=contsueldo+sueldo[x]
    print("El total de sueldos que abona la empresa es: ")
    print(contsueldo)

    print("El promedio de los sueldos")
    promedio=contsueldo//cont
    print(promedio)

    contmec=0
    for x in range(cont):
        if categoria[x]==1:
            contmec=contmec+1

    print("el sueldo promedio de los mecanico")

    suelmec=0
    promsuel=0

    for x in range(cont):
        if sueldo[x]>0 and categoria[x]==1:
            suelmec=suelmec+sueldo[x]
    promsuel=suelmec//contmec
    print(promsuel)

    return archivo


#bloque principal


titulo_subrayado("      PATRON DE INFORMES      ")
archi_abrir()
titulo_subrayado("      FIN DEL PROGRAMA        ")
