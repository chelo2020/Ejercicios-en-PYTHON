#Algoritmo de ordenamiento por selección

lista=[7,8,3,2,1,5,6,9]

longitud=len(lista)

for i in range(longitud-1):
    menor=i
    for j in range(i+1,longitud):
        if lista[j]<lista[menor]:
            menor=j

    aux=lista[menor]
    lista[menor]=lista[i]
    lista[i]=aux

print(lista)



