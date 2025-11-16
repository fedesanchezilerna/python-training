# Ejercicio 4: Validación de Entrada (Medio)
# Pide al usuario un número.
# - Verifica que NO esté vacío
# - Verifica que sea numérico
# - Si es válido, conviértelo a entero y verifica si es par o impar

num = input("Introduce un número: ")

if num != "":
    print("Número no vacío")
    
print(f"Input tipo: {type(num)}")
    
if isinstance(num, str):
    num = int(num)
    print(f"Nuevo type: {type(num)}")