# Ejercicio 7: Validador de Contraseña (Difícil)
# Pide una contraseña y verifica que:
# - NO esté vacía
# - Tenga al menos 8 caracteres
# - NO sea completamente numérica
# - NO sea "password" o "12345678"
# Usa múltiples condiciones con `not`, `and`, y `or`.

password = input("Introduce una contraseña: ")

if password == "" or not len(password) > 7 or password.isnumeric() or password == "password" or password == "12345678":
    print("Contraseña inválida")
else:
    print("Contraseña válida")