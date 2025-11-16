# Ejercicio 8: Comparador de Strings con Lógica (Difícil)
# Pide dos palabras al usuario:
# - Compara si son iguales (case-insensitive)
# - Usa `not` para verificar que NO son exactamente iguales (case-sensitive)
# - Compara cuál es mayor alfabéticamente
# - Si ninguna comienza con vocal, muestra un mensaje especial

palabra1 = input("Introduce una palabra: ")
palabra2 = input("Introduce una palabra: ")

if palabra1 == palabra2:
    print("Palabras iguales")

if ord(palabra1[0]) < ord(palabra2[0]):
    print(f"{palabra1}\n{palabra2}")
else:
    print(f"{palabra2}\n{palabra1}")
    
if (palabra1[0].lower() not in 'aeiou') and (palabra2[0].lower() not in 'aeiou'):
    print("Mensaje especial")