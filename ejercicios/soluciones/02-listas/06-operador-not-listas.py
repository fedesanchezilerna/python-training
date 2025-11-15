# Ejercicio 6: Operador NOT con Listas (Medio-Difícil)
# Crea dos listas: `lista1 = [1, 2, 3]` y `lista2 = [4, 5, 6]`.
# - Usa `not` para verificar si lista1 NO está vacía
# - Verifica si lista1 NO es igual a lista2
# - Crea una lista vacía y usa `not` para comprobar que está vacía

print("Ejercicio 6: Operador NOT con Listas")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(f"La lista1 NO está vacía? {not lista1 == []}")
print(f"La lista1 NO es igual a la lista2? {not lista1 == lista2}")

listaVacia = []
print(f"La lista vacía está vacía? {not listaVacia}")