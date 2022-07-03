#Burbuja mejorado con menor cantidad de
# comparaciones

lista=[7,8,3,2,1,5,6,9]

comparaciones=0

for i in range(len(lista)-1):
    
    for j in range(len(lista)-1-1):
        
        comparaciones=comparaciones+1
        
        if lista[j]<lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux


print(lista)
print(comparaciones)

