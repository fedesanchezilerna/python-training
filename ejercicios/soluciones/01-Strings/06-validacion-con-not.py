# Ejercicio 6: Validación con NOT (Medio-Difícil)
# Crea un programa que pida una contraseña al usuario. La contraseña es válida si:
# - NO está vacía
# - NO es completamente numérica
# - NO es menor de 6 caracteres
# Usa el operador `not` en las validaciones.

print("Ejercicio 6: Validación con NOT")

password = input("Ingresa una contraseña: ")

if not password == "" and not password.isnumeric() and not len(password) < 6:
    print(f"Contraseña guardada: {password}")
else:
    print("Contraseña inválida")