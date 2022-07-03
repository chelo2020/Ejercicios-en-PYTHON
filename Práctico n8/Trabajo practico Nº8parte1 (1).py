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
#4) Se solicita 1 Grabar 2- cancelar (en el caso de grabar se genera el archivo de
# novedad según diseño Fig 3) .

#ejercicio 3:

fila=[]
cont=0
for x in range(4):
    columnas=[]
    fila.append(columnas)
    for k in range(3):
        cont=cont+1
        columnas.append(cont)
for x in range(4):
    print("valor de la fila",x,": ")
    print(*fila[x])
        