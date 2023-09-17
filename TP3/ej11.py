#Dada una lista de diccionarios que contienen .
#información de estudiantes de una materia 
#(nombre_apellido, legajo, nota_parcial1, nota_parcial2, nota_final),
# crea una lista que contenga los nombres de todos los
# estudiantes que han obtenido una calificación superior a 90
# en al menos un examen utilizando list comprehensions.

from faker import Faker

def crear_registro_ficticio():
    fake = Faker()
    
    nombre_apellido = fake.name()
    legajo = fake.unique.random_int(min=10000, max=99999)
    nota_parcial1 = fake.random_int(min=0, max=100)
    nota_parcial2 = fake.random_int(min=0, max=100)
    nota_final = (nota_parcial1 + nota_parcial2) // 2
    
    registro = {
        "nombre_apellido": nombre_apellido,
        "legajo": legajo,
        "nota_parcial1": nota_parcial1,
        "nota_parcial2": nota_parcial2,
        "nota_final": nota_final
    }
    
    return registro

# Ejemplo de uso de la función para generar un registro ficticio

newList = []
for i in range(30):
    newList.append(crear_registro_ficticio())

print([reg for reg in newList if reg["nota_final"] >= 90])
