#%%
#Retorna mayúscula las letras impares y minúsculas las pares
def myfunc(palabra):
    largo=len(palabra)
    i=0
    resultado=""
    while i<largo:
        if i%2==0:
            resultado=resultado+palabra[i].lower()
        else:
            resultado=resultado+palabra[i].upper()
        i=i+1
  
    return resultado

#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both
#  numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b)
    elif a%2!=0 and  b%2!=0:
        return max(a,b)


#ANIMAL CRACKERS: Write a function takes a two-word string and returns 
# True if both words begin with same letter
def animal_crackers(palabra):
    lista=palabra.split()
    return lista[0][0].lower() == lista [1][0].lower()


#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
# or if one of the integers is 20. If not, return False
def makes_twenty(a,b):
    if sum((a,b))==20:
        return True
    elif a==20 or b==20:
        return True
    else:
        return False



#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(palabra):
    resultado=""
    largo=len(palabra)
    if largo > 4:
        resultado=resultado+palabra[0].upper()
        resultado=resultado+palabra[1:3]
        resultado=resultado+palabra[3].upper()
        resultado=resultado+palabra[4:largo]
        return resultado
    else:
        "Se necesita una palabra con un mínimo de 4 caractéres"
    
#old_macdonald("macdonald")



#MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(frase):
    lista=frase.split()
    return " ".join(lista[::-1])



#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(a):
    if abs(200-a) <=10:
        return True
    if abs(100-a) <=10:
        return True
    else:
        return False


#has 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(lista):
    i=0
    for elemento in lista:
        if elemento==3:
            return lista[i+1]==3
        i=i+1


#SPY GAME: Write a function that takes in a list of integers 
# and returns True if it contains 007 in order

def spy_game(lista):
    i=0
    posiciones=[] 
    for elemento in lista:
        if elemento==7:
            posiciones.append(i)
        i=i+1   
    for elemento in posiciones:
        return lista[elemento-1]==0 and lista[elemento-2]==0 and elemento-1>=0 and elemento-2>=0


#COUNT PRIMES: Write a function that returns the number of prime numbers
#  that exist up to and including a given number

def count_primes(num):
    lista=list(range(1,num+1))
    resultado=[]
    for i in lista:
        primo=False
        for j in lista:
            if i>j:
                if i%j==0 and i!=j and j!=1: 
                    primo=False
                elif j==1:
                    primo=True
        if primo==True:
            resultado.append(i)    
        i=i+1    
    return len(resultado)
count_primes(541)

def Saluda():
    return ("Hola")
