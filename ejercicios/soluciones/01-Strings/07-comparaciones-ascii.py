# Ejercicio 7: Comparaciones ASCII (Difícil)
# Escribe un programa que:
# - Pida dos palabras al usuario
# - Compare cuál es "mayor" alfabéticamente
# - Muestre el código ASCII del primer carácter de cada palabra
# - Explique por qué una es mayor que la otra

print("Ejercicio 7: Comparaciones ASCII")

palabra1 = input("Ingresa palabra1: ")
palabra2 = input("Ingresa palabra2: ")

print(f"Código ASCII palabra1: {ord(palabra1[0])}")
print(f"Código ASCII palabra2: {ord(palabra2[0])}")

if palabra1 > palabra2:
    print(f"Razón: '{palabra1[0]}' ({ord(palabra1[0])}) > '{palabra2[0]}' ({ord(palabra2[0])})")
elif palabra1 < palabra2:
    print(f"Razón: '{palabra2[0]}' ({ord(palabra2[0])}) > '{palabra1[0]}' ({ord(palabra1[0])})")
else:
    print(f"\nAmbas letras son iguales")