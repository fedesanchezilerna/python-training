# Ejercicio 1: Métodos Básicos de Cadenas (Fácil)
# Crea una variable `mensaje` con el texto "bienvenido a python" y muestra:
# - El mensaje con la primera letra en mayúscula
# - El mensaje completamente en mayúsculas
# - El mensaje completamente en minúsculas
# - Si el mensaje comienza con "bien"
# - Cuántas veces aparece la letra "n"

print("Ejercicio 1: Métodos Básicos de Cadenas")

mensaje = "bienvenido a python"

print(f"Primera letra en mayúscula: {mensaje.capitalize()}")

# El mensaje completamente en mayúsculas
print(f"Mensaje en mayúsculas: {mensaje.upper()}")

# El mensaje completamente en minúsculas
print(f"Mensaje en minúsculas: {mensaje.lower()}")

# Si el mensaje comienza con "bien"
print(f"Comienza con 'bien'? {mensaje.startswith('bien')}")

# Cuántas veces aparece la letra "n"
print(f"La letra 'n' aparece {mensaje.count('n')} veces")