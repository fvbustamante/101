#%%
myfile=open("ip.txt")

# read() retorna un string gigante de todo lo que hay en el archivo
# read() solo se lee una vez por ejecución, a menos que se haga
# un reset del contador: myfile.seek(0)


# myfile.read()
# myfile.seek(0)


# read() retorna un string gigante de todo lo que hay en el archivo
# read() solo se lee una vez por ejecución, a menos que se haga
# un reset del contador: myfile.seek(0)
# Readlines() tiene una lista con cada linea leida


# myfile.readlines()

#openfile puede recibir el path del archivo que hay que leer.

#Los archivos se deben cerrar. Por ejemplo, si posteriormente se tienen que
#borrar

myfile.close()

# con with no es necesario cerrar el archivo (Se cierra solo)
# with open("ip.txt", "r") as f:
#     lista = f.readlines()
#     print(lista)


with open('salida.txt','w',encoding="utf-8") as f:
    f.write("Primera linea\n")
    f.write("Segunda linea\n")

with open("salida.txt", "a",encoding="utf-8") as f:
    f.write("Linea añadida, es posible escribir ñ y á por utf8, ascii no lo permite\n",)


# r : readonly
# w : write only, usar utf-8 para caracteres especiales
# a : agrega a un archivo existente