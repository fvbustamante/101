
#%%
10%1
print (5%2)
#%%


def repeatedString(s, n):
    lista = s
    contador_a=0
    
    largo=len(lista)
    for letra in lista:
        if letra=='a':
            contador_a=contador_a+1
    
    if n%largo==0:
        resto= n%largo
    elif lista[n%largo-1]=='a':
        resto=1

    total= int(n/largo)*contador_a+resto
   
    return total





#%%

def countingValleys(s):
    lista=[]
    acum=0
    previo=0
    contador=0
    for item in s:
        if item=="U":
            lista.append(1)
        elif item=="D":
            lista.append(-1)
    
    for item in lista:
        previo=acum
        acum=acum+item
        if acum ==0 and previo<0:
            contador=contador+1
    return contador

countingValleys("DUDU")

#%%

lista=[]
# 10 20 20 10 10 30 50 10 20

lista.append(10)
lista.append(20)
lista.append(20)

lista.append(10)
lista.append(10)
lista.append(30)

lista.append(50)
lista.append(10)
lista.append(20)

unico=set()
for item in lista:
    unico.add(item)

contador=0
parcial=0
for item in unico:
    contador=0
    for elemento in lista:
        
        if item==elemento:
            contador=contador+1
    if contador>1 and contador%2==0:
        parcial=parcial+contador/2
    elif contador>1 and contador%2!=0:
        parcial= parcial+int(contador/2)

print(int(parcial))

#%%

def jumpingOnClouds(c):

    posiciones=[]
    i=0
    lista=[]
    for elemento in c:
        if elemento !=" ":
            lista.append(elemento)
    print (c)
    for elemento in lista:
        if elemento=='1':
            posiciones.append(i)
        i=i+1
    indice=0
    termino=len(lista)-1
    contador=0
    print(posiciones)
    while indice < termino:
        if indice+2 not in posiciones and indice+2<=termino:
            print("i1",indice,contador,termino)
            indice=indice+2
            contador=contador+1
        elif indice+1 in posiciones and indice+1 <=termino:
            print("i2",indice,contador,termino)
            indice=indice+2
            contador=contador+1
        elif indice+1 not in posiciones and indice+1<=termino:
            print("i3",indice,contador,termino)
            indice=indice+1
            contador=contador+1
    return contador
        
        

a=jumpingOnClouds("0101000000000010")
print ("contador:",a)

#%%
def timeConversion(s):
    lista=[]
    lista=s.split(":")
    hora=int(lista[0])
    min=(lista[1])
    seg=lista[2][:2]
    string=lista[2][2:]   
    
    if string=="PM":
        hora=hora+12
    elif string=="AM":
        pass

    return str(hora)+":"+min+":"+str(seg)
    
        





timeConversion("07:56:43PM")

#%%

def countDuplicates(numbers):

    unico=set()
    acumulador=[]
    entrada=[]
    for elemento in numbers[1:]:
        unico.add(elemento)
    for elemento in numbers[1:]:
        entrada.append(elemento)
    for elemento in unico:
        contador=0
        contador=entrada.count(elemento)
        print(contador)
        if contador>1:
            acumulador.append(contador)
  
    return len(acumulador)
 



countDuplicates(entrada1)


