# Ejercicio 9: Lista con Range (Difícil)
# - Crea una lista con números del 1 al 20 usando `range()`
# - Cuenta cuántos números pares hay (pista: usa un bucle o count con módulo)
# - Muestra solo los primeros 5 elementos
# - Muestra solo los últimos 5 elementos

listaRange = list(range(1, 20))

# Contar números pares
pares = sum(1 for num in listaRange if num % 2 == 0)

# Mostrar primeros 5 elementos
print("Primeros 5:", listaRange[:5])

# Mostrar últimos 5 elementos
print("Últimos 5:", listaRange[-5:])

# Mostrar cantidad de pares
print("Números pares:", pares)