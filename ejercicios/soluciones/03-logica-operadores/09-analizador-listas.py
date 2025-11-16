# Ejercicio 9: Analizador de Listas (Difícil)
# Crea una lista `datos = [10, 20, 30, 40, 50]`.
# - Verifica que la lista NO esté vacía
# - Verifica que el primer elemento NO sea cero
# - Verifica que la longitud sea exactamente 5
# - Si todas las condiciones son True, suma todos los elementos

datos = [10, 20, 30, 40, 50]

if not datos == [] and not datos[0] == 0 and len(datos) == 5:
    print(f"Suma datos: {sum(datos)}")
