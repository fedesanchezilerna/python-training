# Ejercicio 5: Análisis de Texto (Medio)
# Crea una variable `frase = "Python es genial"`.
# - Cuenta cuántas veces aparece la letra "e"
# - Verifica si la frase comienza con "Python"
# - Convierte la frase a mayúsculas y guárdala en otra variable
# - Compara ambas variables usando `==` y `!=`

print("Ejercicio 5: Análisis de Texto")

frase = "Python es genial"

print(f"La letra 'e' aparece {frase.count('e')} veces")

print(f"La frase comienza con 'Python': {frase.startswith('Python')}")

fraseMayusculas = frase.upper()
print(f"Frase original en mayúsculas:\n{fraseMayusculas}")

print(f"Las frases son iguales: {frase == fraseMayusculas}")
print(f"Las frases son diferentes: {frase != fraseMayusculas}")