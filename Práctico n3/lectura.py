arch=open("archivo.txt","r")
#defino las variables tipo lista que voy a utilizar
codemp=[] #codigo empleado
nomemp=[] #nombre y apellido del empleado
edad=[] #edad
sexo=[] #sexo
ecivil=[] #estado civil
cont=0 #contador de la cantidad de empleados
lista=arch.readline()
lineas=lista.split(",")
while lista!="":
    lineas=lista.split(",")
    cont=cont+1
    lista1=int(lineas[0])
    codemp.append(lista1)
    lista2=lineas[1]
    nomemp.append(lista2)
    lista3=int(lineas[2])
    edad.append(lista3)
    lista4=int(lineas[3])
    sexo.append(lista4)
    lista5=int(lineas[4])
    ecivil.append(lista5)
    lista=arch.readline()
arch.close()

for x in range(cont):
    print(codemp[x],nomemp[x],edad[x],sexo[x],ecivil[x])
    print("------------------------------------")


#ordeno alfabeticamente las listas creadas
rango=cont-1
for k in range(rango):
    for x in range(rango-k):
        if nomemp[x]>nomemp[x+1]:
            aux=nomemp[x]
            aux1=codemp[x]
            aux2=edad[x]
            aux3=sexo[x]
            aux4=ecivil[x]
            nomemp[x]=nomemp[x+1]
            codemp[x]=codemp[x+1]
            edad[x]=edad[x+1]
            sexo[x]=sexo[x+1]
            ecivil[x]=ecivil[x+1]
            nomemp[x+1]=aux
            codemp[x+1]=aux1
            edad[x+1]=aux2
            sexo[x+1]=aux3
            ecivil[x+1]=aux4
#cuento la cantidad de empleados varon(contvar) y
#la cantidad de empleadad mujeres solteras(contms), mujeres entre 20 y 30(mop1)
# mujeres casadas entre 30 y 40 años(mop2), Cantidad de mujeres casadas(mop3)
#Total de varones solteros con edad de 25 años(vop1),  Total de varones casados(vop2).
contms=0 #contador de cantidad de mujeres solteras
contvar=0 #contador de cantidad de varones
mop1=0 #contador de cantidad de mujeres entre 20 y 30 años
mop2=0 #contador de cantidad de mujeres entre 30 y 40
mop3=0 #contador de cantidad de mujeres casadas
vop1=0 #contador de cantidad de cotador de varones soltero con 25 años
vop2=0 #contador de cantidad de varones solteros
for x in range(cont):
    if sexo[x]==2 and ecivil[x]==1:
        contms=contms+1
    if sexo[x]==1:
        contvar=contvar+1
    if sexo[x]==2:
        if edad[x]>19:
            if edad[x]<31:
                mop1=mop1+1
    if sexo[x]==2:            
        if edad[x]>29:
            if edad[x]<41:
                mop2=mop2+1
    if sexo[x]==2 and ecivil[x]==2:
        mop3=mop3+1
    if sexo[x]==1 and edad[x]==25:
        vop1=vop1+1
    if sexo[x]==1 and ecivil[x]==1:
        vop2=vop2+1               

#imprimo la cantidad de personal agregado, la cantidad de varones y
#la cantidad de mujeres solteras
#por otro lado, si la cantidad de mujeres solteras es 0 me tira otra leyenda
print("-----------------------------")#separador
print("la cantidad de empleados que listo fueron:",cont)
print("la cantidad de empleados varones es de: ", contvar)
if contms>0:
    print("la cantidad de trabajadores mujerer y solteras es de:")
    print(contms)
else:
    print("no hay trabajadores del sexo femenino con el estado civil como solteras")
print("------------------------------")#separador

#imprimo la lista de empleados ordenados alfabeticamente
print("el padron queda conformado alfabeticamente de la siguiente manera")
for x in range(cont):
    print("codigo de empleado: ",codemp[x])
    print("nombre: ",nomemp[x])
    print("edad: ",edad[x])
    if sexo[x]==1:
        print("sexo: varon")
    else:
        print("sexo: mujer")
    print("////////////////////////////////////")#separador de lista
print("la cantidad total de empleados es: ", cont)
print("-------------------------------------------")#separador
print("Cantidad de mujeres entre 20 y 30 años: ",mop1)
print("Cantidad de mujeres casadas entre 30 y 40 años: ",mop2)
print("Cantidad de mujeres casadas: ",mop3)
print("Total de varones: ",contvar)
print("Total de varones solteros con edad de 25 años: ",vop1)
print("Total de varones casados: ", vop2)