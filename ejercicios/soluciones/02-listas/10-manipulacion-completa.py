# Ejercicio 10: Manipulación Compleja (Difícil)
# Crea una lista `numeros = [3, 7, 3, 9, 3, 7, 3, 5]`.
# - Cuenta todas las apariciones de cada número único
# - Calcula el total de elementos
# - Determina qué número es el más frecuente
# - Usa el operador `not` para verificar que el número 10 NO está en la lista

numeros = [3, 7, 3, 9, 3, 7, 3, 5]

# Cuenta todas las apariciones de cada número único
frecuencias = {}
for num in numeros:
    frecuencias[num] = frecuencias.get(num, 0) + 1

print("Frecuencias:", frecuencias)
print("Frecuencias type: ", type(frecuencias))

# Calcula el total de elementos
total_elementos = len(numeros)
print("Total de elementos:", total_elementos)

# Determina qué número es el más frecuente
numero_mas_frecuente = max(frecuencias, key=frecuencias.get)
print("Número más frecuente:", numero_mas_frecuente)

# Verifica que el número 10 NO está en la lista
if not 10 in numeros:
    print("El número 10 NO está en la lista")