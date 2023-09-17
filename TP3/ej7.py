#Implemente un programa que le pida una palabra al usuario y
# cuenta la cantidad de vocales en ella. 
#El programa deberá pedirle palabras al usuario hasta que éste introduzca la palabra “salir”.

def isVocal(x):
    rtn = False
    if x.lower() == 'a' or x.lower() == 'e' or x.lower() == 'i' or x.lower() == 'o' or x.lower() == 'u':
        rtn = True
    return rtn

palabra = input("Palabra: ")

while palabra.lower() != "Salir":
    print([letra for letra in palabra if isVocal(letra)])
    palabra = input("Palabra: ")
