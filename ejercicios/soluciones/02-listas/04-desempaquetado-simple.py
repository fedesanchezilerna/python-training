# Ejercicio 4: Desempaquetado Simple (Medio)
# Crea una lista `datos = [18, "Juan", "Pérez", True]`.
# - Desempaqueta la lista en variables: edad, nombre, apellido, estudiante
# - Muestra cada variable con un mensaje descriptivo
# - Usa f-strings para crear una frase con toda la información

print("Ejercicio 4: Desempaquetado Simple")

datos = [18, "Juan", "Pérez", True]

edad, nombre, apellido, estudiante = datos

print(f"edad: {edad}")
print(f"nombre: {nombre}")
print(f"apellido: {apellido}")
print(f"estudiante: {estudiante}")

print(f"Mi nombre es {nombre} {apellido}, tengo {edad} años. Status de estudiante: {estudiante}")