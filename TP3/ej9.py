#Dadas dos listas de números del mismo tamaño,
# crea una nueva lista que contenga la multiplicación de los elementos correspondientes
# de ambas listas utilizando list comprehensions.

lista1 = list(range(1,21))
lista2 = list(range(3,23))

newLista = [x * y for x, y in zip(lista1,lista2)]

print(newLista)