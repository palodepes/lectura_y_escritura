#este programa creara programa electronicos
nombres=["adrian","francisco","sarai","segio","aurelio"]
apellidos=["hernandez","perez","patricio","lezama","hernandez"]
correos=[]
ln=len(nombres)
la=len(apellidos)
if ln==la:
    lista=open("lista.txt","w")
    for i in range(ln):
        correo=nombres[i]+"."+apellidos[i]+"@correo.com"
        correos.append(correo)
        print(correo)
for x in range(ln):
    lista.write(correos[x])
    lista.write("\n")
lista.close()






