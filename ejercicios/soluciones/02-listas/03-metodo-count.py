# Ejercicio 3: Método count() (Medio)
# Crea una lista `valores = [5, 8, 5, 3, 8, 5, 9, 8, 5]`.
# - Cuenta cuántas veces aparece el número 5
# - Cuenta cuántas veces aparece el número 8
# - Muestra la proporción de 5s sobre el total (como porcentaje)

print("Ejercicio 3: Método count()")

valores = [5, 8, 5, 3, 8, 5, 9, 8, 5]

print(f"Número de veces que aparece el 5: {valores.count(5)}")
print(f"Número de veces que aparece el 8: {valores.count(8)}")

def proporcion_porcentaje(list, num):
    return (list.count(num) * 100) / len(list)

print(f"Proporción de 5s en la lista: {proporcion_porcentaje(valores, 5):.2f}%")