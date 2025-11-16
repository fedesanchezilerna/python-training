# Ejercicio 3: Operadores Lógicos AND/OR (Medio)
# Crea variables: `edad = 25`, `es_estudiante = True`.
# - Verifica si edad es >= 18 AND es_estudiante es True
# - Verifica si edad es < 18 OR edad > 65
# - Usa `not` para verificar que NO es menor de edad

edad = 25
es_estudiante = True

if edad >= 18 and es_estudiante:
    print("Prueba 1")
    
if edad < 18 or edad > 65:
    print("Prueba 2")
    
if not edad < 18:
    print("Prueba 3")