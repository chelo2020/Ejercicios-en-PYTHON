#Burbuja mejorado con menor cantidad de
# comparaciones pero ahora contenido con centinela

lista=[7,8,3,2,1,5,6,9]

comparaciones=0
hay_cambios=True
i=0

while hay_cambios and i<len(lista)-1:
    hay_cambios=False
    
    for j in range(len(lista)-1-1):
        
        comparaciones=comparaciones+1
        
        if lista[j]<lista[j+1]:
            aux=lista[j]
            lista[j]=lista[j+1]
            lista[j+1]=aux
            hay_cambios=True

    i=i+1
print(lista)
print(comparaciones)