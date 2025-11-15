# Ejercicio 2: Validación de Datos (Fácil)
# Pide al usuario que ingrese un código. Verifica:
# - Si el código es numérico usando `isnumeric()`
# - Si el código está completamente en mayúsculas
# - La longitud del código

print("Ejercicio 2: Validación de Datos")

# Pedir un código
codigo = input("Ingresa un código: ")

# Verificaciones
print(f"\nResultados")
print(f"El código es numérico: {codigo.isnumeric()}")
print(f"El código está en mayúsculas: {codigo.isupper()}")
print(f"Longitud del código: {len(codigo)}")