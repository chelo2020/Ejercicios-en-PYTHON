#Algoritmo de ordenamiento por selección

lista=[7,8,3,2,1,5,6,9]

longitud=len(lista)

for i in range(longitud-1):
    print(lista)
    menor=i
    print("El indice actual es: ",menor)
    for j in range(i+1,longitud):
        if lista[j]<lista[menor]:
            menor=j
            print("Recorriendo lista, es menor el indice: ",menor)

    aux=lista[menor]
    lista[menor]=lista[i]
    lista[i]=aux
    print("Cambiamos el elemento",lista[menor],"por el elemento",lista[i])
