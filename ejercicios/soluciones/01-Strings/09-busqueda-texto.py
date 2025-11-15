# Ejercicio 9: Búsqueda en Texto (Difícil)
# Crea una variable con tu nombre completo. Escribe un programa que:
# - Cuente cuántas vocales (a,e,i,o,u) hay en tu nombre
# - Use el operador `not` para verificar que NO hay números en el nombre
# - Muestre el nombre con cada palabra capitalizada

print("Ejercicio 9: Búsqueda de Texto")

nombreCompleto = input("Ingrese nombre completo: ")

vocalesNombre = nombreCompleto.lower().count('a') + nombreCompleto.lower().count('e') + nombreCompleto.lower().count('i') + nombreCompleto.lower().count('o') + nombreCompleto.lower().count('u')
print(f"Vocales del nombre: {vocalesNombre}")

# Verifica que NO hay números en el nombre
hayNumeros = any(char.isdigit() for char in nombreCompleto)
print(f"No hay números en el nombre: {not hayNumeros}")

print(f"Nombre con cada palabra capitalizada: {nombreCompleto.title()}")