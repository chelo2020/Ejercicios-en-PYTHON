arch=open("archivo1.txt","r")
#defino las variables tipo lista que voy a utilizar
codemp=[]#lista del codigo del empleado
nomemp=[]#lista del nombre del empleado
sueldo=[]#sueldo del empleado
cat=[] #categoria del empleado
categoria={1:"mecanico",2:"conductor"}#defino un diccionario para la categoria
cont=0 #contador de la cantidad de empleados
#comienzo a leer linea a linea el archivo:
lista=arch.readline()
lineas=lista.split(",")#separo utilizando la "," el contenido de cada linea, para poder comenzar a descomponer y cargar en las variables que defini previamente
while lista!="":#while para que lea linea a linea hasta el final del contenido del archivo
    lineas=lista.split(",")
    cont=cont+1
    lista1=int(lineas[0])
    codemp.append(lista1)
    lista2=lineas[1]
    nomemp.append(lista2)
    lista3=float(lineas[2])
    sueldo.append(lista3)
    lista4=int(lineas[3])
    cat.append(lista4)
    lista=arch.readline()
arch.close()

#realizo la operacion para calcular el promedio de sueldo de todos los empleados
sumsuel=0
promedio=0
promec=0
suelmec=0
contmec=0
for x in range(cont):
    sumsuel=sumsuel+sueldo[x]
    if cat[x]==1:#calculo el promedio de los sueldos de los empleados
        contmec=contmec+1
        suelmec=suelmec+sueldo[x]
promedio=sumsuel/cont    
promec=suelmec/contmec    



print("El padron queda conformado de la siguiente manera: ")
for x in range(cont):
    print(codemp[x],nomemp[x],sueldo[x])
    print("categoria: ",categoria[cat[x]])

print("//////////////////////////////////////////")    
print("La cantidad de empleados listados es de: ",cont)
print("///////////////////////////////////////////")
print("El promedio de sueldos es: $", promedio)
print("")
if contmec>=1:
    print("El promedio de sueldos de los mecanicos es: ",promec)