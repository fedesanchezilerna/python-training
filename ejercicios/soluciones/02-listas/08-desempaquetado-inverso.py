# Ejercicio 8: Desempaquetado Inverso (Difícil)
# Crea una lista `persona = [25, 1.70, "Ana", "García"]`.
# - Desempaqueta en orden normal
# - Desempaqueta en orden inverso usando `[::-1]`
# - Desempaqueta solo el nombre y apellido (ignorando edad y altura)

persona = [25, 1.70, "Ana", "García"]

# Desempaqueta en orden normal
edad, altura, nombre, apellido = persona

# Desempaquetado en orden inverso
apellido_inv, nombre_inv, altura_inv, edad_inv = persona[::-1]

# Desempaquetado solo nombre y apellido (ignorando edad y altura)
_, _, nombre_solo, apellido_solo = persona