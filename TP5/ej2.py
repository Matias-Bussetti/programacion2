pila1 = []

def apilar(pila, elemento):
    pila.insert(0, elemento)

def desApilar(pila):
    return  "Esta Vacia" if esta_vacia(pila) else pila.pop(0) 

def longitud(pila):
    return len(pila)

def esta_vacia(pila):
    return len(pila) == 0

apilar(pila1, 0)
apilar(pila1, 1)
apilar(pila1, 2)
apilar(pila1, 3)
print(pila1)

print(desApilar(pila1))
print(desApilar(pila1))
print(desApilar(pila1))
print(desApilar(pila1))
print(desApilar(pila1))
print(pila1)


