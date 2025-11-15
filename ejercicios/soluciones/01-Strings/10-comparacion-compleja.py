# Ejercicio 10: Comparación Compleja (Difícil)
# Crea tres variables: `a = "abc"`, `b = "ABC"`, `c = "abc"`.
# - Verifica si `a == c` y `a != b`
# - Usa `not` para verificar que `a` NO es mayor que `c`
# - Convierte `b` a minúsculas y compárala con `a`
# - Muestra los resultados explicando cada comparación

print("Ejercicio 10: Comparación Compleja")

a = "abc"
b = "ABC"
c = "abc"

print(f"a == c y a != b? {a == c and a != b}")

print(f"'b' minúsculas es igual a a? {b.lower() == a}")

print(f"'a' NO es mayor que c? {not a > c}")

print(f"\nExplicaciones:")
print(f"- 'abc' == 'abc': True (son idénticas)")
print(f"- 'abc' != 'ABC': True (mayúsculas vs minúsculas)")
print(f"- 'abc' > 'abc': False (son iguales, por eso NO es mayor)")
print(f"- 'ABC'.lower() == 'abc': True (ambas son 'abc')")