# Ejercicio 6: Clasificación Compleja (Difícil)
# Pide al usuario tres calificaciones y clasifícalas:
# - Si todas son >= 7: "Aprobado con buenas notas"
# - Si alguna es < 5: "Reprobado"
# - Si el promedio es >= 6 pero < 7: "Aprobado justo"
# Usa operadores lógicos y el operador `not` donde sea apropiado.

calif1 = int(input("Introduce calificación 1: "))
calif2 = int(input("Introduce calificación 2: "))
calif3 = int(input("Introduce calificación 3: "))

notas = [calif1, calif2, calif3]

if calif1 is 7 and calif1 is calif2 and calif1 is calif3:
    print("Aprobado con buenas notas")
elif any(nota < 5 for nota in notas):
    print("Reprobado")
elif sum(notas) / 3 >= 6:
    print("Aprobado justo")
