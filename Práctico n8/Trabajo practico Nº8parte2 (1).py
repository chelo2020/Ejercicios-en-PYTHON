#         Trabajo practico Nº
#1)Ingresar números en un vector de 10 elementos.
#2)Con los datos ingresados del ejercicio anterior,   
#sumar los valores y determinar la  posición del número mayor.
#3)Cargar una matriz de 4x3 elementos ( M(4,3) ) por filas.
#4)Generar una matriz de 5 filas y 7 columnas, 
#sumar los valores de las filas y los valores de las columnas.
#5)Teniendo en cuenta el ítem 4, sumar los valores de las filas y 
#guardar en un vector columna, sumar las columnas y guardar en un vector fila.
#6)Teniendo en cuenta el ejercicio 32 ítem 5, informar el mayor de la 
#suma del vector columna y el menor de la suma del vector fila.
# Una vez identificado en el vector fila el menor, 
#indicar en que posición se encuentra.

#ejercicio 4:

filas=[]
cont=0
for x in range(5):
    columnas=[]
    filas.append(columnas)
    for k in range(7):
        cont=cont+1
        columnas.append(cont)
for x in range(5):
    print("valor de la fila",x,": ")
    print(*filas[x],"\n\n------------------------------------------")

print("////////////////////////////////////////////////\n#Ejercicio 5:")
#ejercicio 5:
print("SUMA DE FILAS: ")

for x in range(5):
    suma=0
    for k in range(7):
        suma=suma+filas[x][k]
    print("\n##el valor de la suma de la fila", x,"es: ",suma)

print("----------------------------------------------\nSuma de las columnas:")

for x in range(7):
    suma=0
    for k in range(5):
        suma=suma+filas[k][x]
    print("\n##el valor de la suma de la columna", x,"es: ",suma) 

print("////////////////////////////////////////////////\n#Ejercicio 6:\n")

#6)Teniendo en cuenta el ejercicio 32 ítem 5, informar el mayor de la 
#suma del vector columna y el menor de la suma del vector fila.
# Una vez identificado en el vector fila el menor, 
#indicar en que posición se encuentra.

#mayor de columnas:

print("mayor de la sumas de las columnas:")
#guardo los valores de la suma de las columnas en un vector suma_vector_columna
suma_vector_columna=[]
for x in range(7):
    suma=0
    for k in range(5):
        suma=suma+filas[k][x]
    suma_vector_columna.append(suma)

#busco el valor mayor:
mayor=suma_vector_columna[0]
for x in range(6):
    if mayor<suma_vector_columna[x+1]:
        mayor=suma_vector_columna[x+1]
        pos=x+1
    else:
        mayor=suma_vector_columna[x]
        pos=x
print("El mayor de la suma del vector columna es: ",mayor,"\nEs la solumna: ",pos)
print("\n------------------------------------------\n")
#guardo el valor de la suma de las lineas en un vector suma_vector_filas:
suma_vector_filas=[]
for x in range(5):
    suma=0
    for k in range(7):
        suma=suma+filas[x][k]
    suma_vector_filas.append(suma)

#busco el valor mayor:
mayor=suma_vector_filas[0]
for x in range(4):
    if mayor<suma_vector_filas[x+1]:
        mayor=suma_vector_filas[x+1]
        pos=x+1
    else:
        mayor=suma_vector_filas[x]
        pos=x
print("El mayor de la suma del vector fila es: ",mayor,"\nEs la fila: ",pos)
print("********FIN**********")

    




     