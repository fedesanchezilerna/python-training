# Ejercicio 5: Lista Mixta (Medio)
# Crea una lista con tu edad, altura, nombre y apellido (como en las actividades).
# - Muestra la longitud de la lista
# - Accede a cada elemento por su índice
# - Desempaqueta la lista en variables apropiadas
# - Crea una frase presentándote con esos datos

print("Ejercicio 5: Lista Mixta")

lista = [30, 1.80, "Micheal", "Jackson"]

print(f"Primer elemento: {lista[0]}")
print(f"Segundo elemento: {lista[1]}")
print(f"Tercer elemento: {lista[2]}")
print(f"Cuarto elemento: {lista[3]}")

edad, altura, nombre, apellido = lista

print(f"Mi nombre es {nombre} {apellido}, tengo {edad} años y mido {altura:.2f}m")