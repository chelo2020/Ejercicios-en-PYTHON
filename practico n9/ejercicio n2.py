#Ordenamiento de burbuja

lista=[7,8,3,2,1,5,6,9]

for i in range(len(lista)-1):
    print("Comparando: ",lista[j],"con",lista[j+1])
    for j in range(len(lista)-1):
        if lista[j]<lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
            print("Recorriendo",lista[j],"por",lista[j+1])

print(lista)