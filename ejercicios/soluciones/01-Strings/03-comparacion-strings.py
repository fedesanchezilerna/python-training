# Ejercicio 3: Comparación de Cadenas (Medio)
# Crea dos variables: `palabra1 = "Manzana"` y `palabra2 = "manzana"`.
# - Compara si son iguales
# - Usa el operador `not` para verificar si NO son iguales
# - Muestra los códigos ASCII del primer carácter de cada una usando `ord()`
# - Explica en un comentario por qué "M" es diferente de "m"

print("Ejecicio 3: Comparación de Cadenas")

palabra1 = "Manzana"
palabra2 = "manzana"

print(f"Palabras iguales: {palabra1 == palabra2}")
print(f"Código ASCII de '{palabra1[0]}': {ord(palabra1[0])}")
print(f"Código ASCII de '{palabra2[0]}': {ord(palabra2[0])}")

# "M" (77) es diferente de "m" (109) porque Python es case-sensitive
# Cada letra tiene su propio código ASCII