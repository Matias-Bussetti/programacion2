from functools import reduce

# complete con su fecha de nacimiento, nombre , legajo y dni
# Al finalizar subir el archivo al aula virtual.
mifecha = "30-01-2001"
minombre = "Matias Ezequiel Bussetti"
milegajo = 21731
midni = 43263841
# 1) implemente una funcion hashFecha(stringfecha) y sume el numero del día, el numero del mes y el numero del año y devuelva el resto de dividirlo por 4.
# ejemplo fecha 01-01-1984 = (01+ 01 +1984) % 4 = 1986 % 4 = 2


def hashFecha(stringfecha):
    day = int(stringfecha[0:2])
    month = int(stringfecha[3:5])
    year = int(stringfecha[6:10])
    return (day + month + year) % 4


# print(hashFecha(mifecha))


# 2) Explique el funcionamiento y describa el algoritmo del ordenamiento burbuja.
# Funcionamiento: Teniendo una lista...
# Algoritmo: ...compara...

# Teniendo una lista de elementos numericos desordenados compara estos elementos n (siendo el total de elementos en ella)
# ~n*n cantidad de veces, en cada una de las repeticiones se logra que los elementos de un extremo queden ordenados.
# Se realiza una comparacion y un intercambio por cada bucle. Las repeticiones van de n a n-1, y se compraran los ementos en la posición i y i+1


# 3 )  Usando el archivo CSV "datos.csv" que contiene información sobre productos. El archivo tiene el siguiente formato:
# Nombre, Precio, Cantidad
# Producto1, 10.99, 50
# Producto2, 5.99, 30
# Producto3, 8.49, 75

# Crea una lista de diccionarios donde cada diccionario represente un producto. Los diccionarios deben tener tres claves: "Nombre" del tipo string, "Precio" del tipo float
# y "Cantidad" del tipo entero, y  los valores deben corresponder a los datos del archivo CSV
archivoPath = "g:\Git Clone\programacion2\PracticaParcial\datos.csv"


def crearStock(archivo):
    lista = []
    for line in open(archivo, "r"):
        if line != "\s":
            lineSplited = line.replace("\n", "").split(",")
            lista.append(
                dict(
                    {
                        "nombre": lineSplited[0],
                        "precio": float(lineSplited[1]),
                        "cantidad": int(lineSplited[2]),
                    }
                )
            )

    return lista


# print(crearStock(archivoPath))


# 4) Crear dos funcion que utilizando la estructura del punto 3. Una que nos devuelva el producto mas caro y la otra que nos devuelva el producto con menor cantidad.
def productoMasCaro(lista):
    prodMasCaro = lista[0]
    for item in lista[1:]:
        if prodMasCaro["precio"] < item["precio"]:
            prodMasCaro = item
    return prodMasCaro


# print(
#    productoMasCaro(crearStock("archivoPath))
# )


def productoMenorCantidad(lista):
    prodEscaso = lista[0]
    for item in lista[1:]:
        if prodEscaso["cantidad"] > item["cantidad"]:
            prodEscaso = item
    return prodEscaso


# print(
#    productoMenorCantidad(
#        crearStock(archivoPath)
#    )
# )


# 5) Implemente una funcion que nos devuelva el total de la posible ganancia. Esto es, Cantidad * Precio para cada producto y que sume todos los resultados. (¿Se puede usar reduce? Fundamente)
def totalGanancia(lista):
    gananciaTotal = 0
    for item in lista:
        gananciaTotal = gananciaTotal + item["cantidad"] * item["precio"]
    return gananciaTotal


# Desconosco la forma de usar reduce
print(totalGanancia(crearStock(archivoPath)))
