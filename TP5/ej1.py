cola1 = []

def encolar(cola, elemento):
    cola.append(elemento)

def desencolar(cola):
    return cola.pop(0) if not esta_vacia(cola) else "No Hay Nada"

def logitud(cola):
    return len(cola)

def esta_vacia(cola):
    return logitud(cola) == 0 

print(cola1)
encolar(cola1, 1)
encolar(cola1, 2)
encolar(cola1, 3)
print(cola1)
print(desencolar(cola1))
print(cola1)
print(desencolar(cola1))
print(cola1)
print(desencolar(cola1))
print(cola1)
print(desencolar(cola1))
print(cola1)