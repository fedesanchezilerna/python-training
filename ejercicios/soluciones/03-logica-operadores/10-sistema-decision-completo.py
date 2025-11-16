# Ejercicio 10: Sistema de Decisión Completo (Muy Difícil)
# Crea un mini-programa que:
# - Pida nombre, edad, y si es estudiante
# - Valide que el nombre NO esté vacío y NO sea numérico
# - Valide que la edad sea un número entre 0 y 120
# - Determine el precio de una entrada:
#   - Menores de 12 o mayores de 65: $5
#   - Estudiantes entre 12 y 25: $8
#   - Otros: $12
# - Use `not`, `and`, `or` en las validaciones

nombre = input("Ingresa nombre: ")
edad = int(input("Ingresa edad: "))
es_estudiante = bool(input("Es estudiante? "))

if nombre != "" and not nombre.isalnum():
    print("Nombre inválido")
elif edad < 0 or edad > 120:
    print("Edad inválida")
else:
    if edad < 12 or edad > 65:
        print("Entrada: $5")
    elif edad > 12 and edad < 25 and es_estudiante:
        print("Entrada: $8")
    else:
        print("Entrada: $12")
        
        