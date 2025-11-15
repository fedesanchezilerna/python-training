# Ejercicio 4: Operador NOT con Strings (Medio)
# Crea una variable `nombre = ""` (cadena vacía).
# - Usa `not` para verificar si el nombre está vacío
# - Pide al usuario un nombre, y usa `not` para verificar si NO comienza con "A"
# - Usa `not` para verificar si el nombre NO contiene solo números

print("Ejercicio 4: Operador NOT con strings")

nombre = ""

print(f"Nombre está vacío? {not nombre}")

nombre = input("Ingresa tu nombre: ")

print(f"NO comienza con 'A'? {not nombre.startswith('A')}")
print(f"NO contiene solo números? {not nombre.isnumeric()}")